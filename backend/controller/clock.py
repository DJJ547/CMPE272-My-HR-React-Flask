from models.employee import Employee
from models.shift import Shift
from flask import session
import datetime
from config import app


def process_punch(punch_type, time_str):
    employee = Employee(app.redis.get('employee_no'))

    # # first shift on 10/27 from 3pm to 9:30pm
    # first_shift_start_time = datetime.datetime(2023, 11, 9, 16, 20)
    # first_shift_end_time = datetime.datetime(2023, 11, 9, 21, 30)
    # first_shift = Shift(first_shift_start_time, first_shift_end_time)
    # # second shift on 10/28 from 9am to 7pm
    # second_shift_start_time = datetime.datetime(2023, 10, 28, 9, 00)
    # second_shift_end_time = datetime.datetime(2023, 10, 28, 19, 00)
    # second_shift = Shift(second_shift_start_time, second_shift_end_time)
    # shifts = [first_shift, second_shift]

    # Employee attributes in order: employee_no, first_name, last_name, birthdate, gender, hire_date, shifts
    # em1 = Employee(1, 'David', 'Dai', datetime.datetime(1994, 5, 20), 'M', datetime.datetime(2023, 9, 10), shifts)
    output = {}
    if punch_type == 'start_shift':
        output = employee.start_shift(time_str, punch_type)
    elif punch_type == 'start_lunch':
        output = employee.start_lunch(time_str, punch_type)
    elif punch_type == 'end_lunch':
        output = employee.end_lunch(time_str, punch_type)
    elif punch_type == 'end_shift':
        output = employee.end_shift(time_str, punch_type)
    print(output)
    return output
