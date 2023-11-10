import datetime
from datetime import timedelta
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, DATE, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect with database
host = 'localhost'
port = 3306
username = 'root'
# remember to replace @ sign with %40 for sqlalchemy to process if ur pw contains @
password = 'Djj%4019950420'
database = 'employees'
# Connect to the database
engine = create_engine("mysql+mysqlconnector://" + username + ":" + password + "@" + host + ":" + str(port) + "/" + database)

Base = declarative_base()


class Employee(Base):

    __tablename__ = "employees"

    emp_no = Column("emp_no", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    birth_date = Column("birth_date", DATE)
    gender = Column("gender", Enum)
    hire_Date = Column("hire_date", DATE)

    def __init__(self, employee_no, first_name, last_name, birthdate, gender, hire_date, shifts):
        self.employee_no = employee_no
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.hire_date = hire_date
        self.shifts = shifts

    # this method tells python how to print objects of this class
    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', employee_number='%s')>" % (
                            self.first_name, self.last_name, self.employee_no)

    def start_shift(self, clock_in_time):
        res = {}
        time = clock_in_time.strftime("%H:%M:%S")
        print("time:", time)
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_actual_start_time_on_time(clock_in_time):
                shift.set_actual_start_time(clock_in_time)
                res['error'] = False
                res['message'] = "shift started at " + time
                return res
            if shift.check_actual_start_time_late(clock_in_time):
                shift.set_actual_start_time(clock_in_time)
                shift.is_late = True
                res['error'] = False
                res['message'] = "shift started late at " + time
                return res
        res['error'] = True
        res['message'] = "shift cannot start"
        return res

    def end_shift(self, clock_out_time):
        res = {}
        time = clock_out_time.strftime("%H:%M:%S")
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_actual_end_time(clock_out_time):
                shift.set_actual_end_time(clock_out_time)
                res['error'] = False
                res['message'] = "shift ended at " + time
                return res
        res['error'] = True
        res['message'] = "shift cannot end"
        return res

    def start_lunch(self, lunch_start_time):
        res = {}
        time = lunch_start_time.strftime("%H:%M:%S")
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_actual_lunch_start_time(lunch_start_time):
                shift.set_actual_lunch_start_time(lunch_start_time)
                res['error'] = False
                res['message'] = "lunch started at " + time
                return res
        res['error'] = True
        res['message'] = "lunch cannot start"
        return res

    def end_lunch(self, lunch_end_time):
        res = {}
        time = lunch_end_time.strftime("%H:%M:%S")
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_actual_lunch_end_time(lunch_end_time):
                shift.set_actual_lunch_end_time(lunch_end_time)
                res['error'] = False
                res['message'] = "lunch ended at " + time
                return res
        res['error'] = True
        res['message'] = "lunch cannot end"
        return res
