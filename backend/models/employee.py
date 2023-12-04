from datetime import datetime
from datetime import timedelta
from config import app

from models.shift import Shift

def convert_datetime_to_string(dtime):
    if not dtime:
        return None
    dstring = ''
    if isinstance(dtime, datetime):
        dstring = dtime.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(dtime, timedelta):
        dstring = str(dtime)
    return dstring


def convert_string_to_datetime(dstring, dtype):
    if not dstring:
        return None
    dtime = None
    if dtype == 'datetime':
        dtime = datetime.strptime(dstring, '%Y-%m-%d %H:%M:%S')
    elif dtype == 'timedelta':
        dtime = datetime.strptime(dstring, '%H:%M:%S')
        dtime = timedelta(hours=dtime.hour, minutes=dtime.minute, seconds=dtime.second)
    return dtime


class Employee:
    def __init__(self, employee_no):
        # open database connection, and fetch data from database
        cur = app.mysql.connection.cursor()
        cur.execute("SELECT * FROM employees WHERE emp_no = %s", (employee_no,))
        user = cur.fetchone()
        cur.close()
        self.employee_no = employee_no
        self.first_name = user[2]
        self.last_name = user[3]
        self.birthdate = user[1]
        self.gender = user[4]
        self.hire_date = user[5]
        self.profile_pic = user[6]
        self.motto = user[7]
        # self.shifts = self.get_shifts_from_db()

    # this method tells python how to print objects of this class
    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', employee_number='%s')>" % (
                            self.first_name, self.last_name, self.employee_no)

    def get_shifts_from_db(self):
        shifts = []
        cur = app.mysql.connection.cursor()
        cur.execute("SELECT assign_shift_start, assign_shift_end FROM shifts WHERE emp_no = %s", (self.employee_no,))
        db_shifts = cur.fetchall()
        cur.close()
        for db_shift in db_shifts:
            shifts.append(Shift(self.employee_no, db_shift[0], db_shift[1]))
        return shifts

    def start_shift(self, clock_in_time_str, punch_type):
        clock_in_time_dtime = convert_string_to_datetime(clock_in_time_str, 'datetime')
        response = {'error': True, 'message': f'shift cannot start at {clock_in_time_str}'}
        # loop thru each shift and find the current one
        print(self.shifts)
        for shift in self.shifts:
            if shift.check_if_is_current_shift(clock_in_time_dtime, punch_type):
                result = shift.set_actual_start_time(clock_in_time_dtime)
                response['error'] = result[0]
                response['message'] = result[1]
        return response

    def end_shift(self, clock_out_time_str, punch_type):
        clock_out_time_dtime = convert_string_to_datetime(clock_out_time_str, 'datetime')
        response = {'error': True, 'message': f'shift cannot end at {clock_out_time_str}'}
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_if_is_current_shift(clock_out_time_dtime, punch_type):
                result = shift.set_actual_end_time(clock_out_time_dtime)
                response['error'] = result[0]
                response['message'] = result[1]
        return response

    def start_lunch(self, lunch_start_time_str, punch_type):
        lunch_start_time_dtime = convert_string_to_datetime(lunch_start_time_str, 'datetime')
        response = {'error': True, 'message': f'lunch cannot start at {lunch_start_time_str}'}
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_if_is_current_shift(lunch_start_time_dtime, punch_type):
                result = shift.set_actual_lunch_start_time(lunch_start_time_dtime)
                response['error'] = result[0]
                response['message'] = result[1]
        return response

    def end_lunch(self, lunch_end_time_str, punch_type):
        lunch_end_time_dtime = convert_string_to_datetime(lunch_end_time_str, 'datetime')
        response = {'error': True, 'message': f'lunch cannot end at {lunch_end_time_str}'}
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_if_is_current_shift(lunch_end_time_dtime, punch_type):
                result = shift.set_actual_lunch_end_time(lunch_end_time_dtime)
                response['error'] = result[0]
                response['message'] = result[1]
        return response

    def update_profile(self, motto, profile_pic_url):
        conn = app.mysql.connection
        cur = conn.cursor()
        try:
            cur.execute("UPDATE employees SET motto = %s, profile_pic = %s WHERE emp_no = %s",
                        (motto, profile_pic_url, self.employee_no))
            conn.commit()
            return {'error': False, 'message': 'Profile updated successfully'}
        except Exception as e:
            conn.rollback()
            return {'error': True, 'message': str(e)}
        finally:
            cur.close()