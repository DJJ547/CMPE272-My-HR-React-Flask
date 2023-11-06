from models.employee import Employee
from models.shift import Shift
import datetime


def process_punch(punch_type, js_time):
    # first shift on 10/27 from 3pm to 9:30pm
    first_shift_start_time = datetime.datetime(2023, 11, 4, 1, 00)
    first_shift_end_time = datetime.datetime(2023, 11, 4, 21, 30)
    first_shift = Shift(first_shift_start_time, first_shift_end_time)
    # second shift on 10/28 from 9am to 7pm
    second_shift_start_time = datetime.datetime(2023, 10, 28, 9, 00)
    second_shift_end_time = datetime.datetime(2023, 10, 28, 19, 00)
    second_shift = Shift(second_shift_start_time, second_shift_end_time)
    shifts = [first_shift, second_shift]

    # Employee attributes in order: employee_no, first_name, last_name, birthdate, gender, hire_date, shifts
    em1 = Employee(1, 'David', 'Dai', datetime.datetime(1994, 5, 20), 'M', datetime.datetime(2023, 9, 10), shifts)
    datetime_time = datetime.datetime.fromtimestamp(js_time/1000.0)
    output = {}
    if punch_type == 'start_shift':
        output = em1.start_shift(datetime_time)
    elif punch_type == 'start_lunch':
        output = em1.start_lunch(datetime_time)
    elif punch_type == 'end_lunch':
        output = em1.end_lunch(datetime_time)
    elif punch_type == 'end_shift':
        output = em1.end_shift(datetime_time)
    print(output)
    return output
