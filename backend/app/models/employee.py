import datetime
from datetime import timedelta

class Employee:
    def __init__(self, employee_no, first_name, last_name, birthdate, gender, hire_date, shifts):
        self.employee_no = employee_no
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.hire_date = hire_date
        self.shifts = shifts

    def check_if_shift_exist(self, time):
        for shift in self.shifts:
            if shift.start_time - time:

    def start_shift(self, clock_in_time):
        for shift in self.shifts:
            if
        if clock_in_time < self.start_time or clock_in_time > self.end_time:
            print('Oops, You dont have any shift assigned this time.')
            return
        if clock_in_time > self.start_time:
            self.check_if_late = True
        self.clock_in_time = clock_in_time

    def end_shift(self, clock_out_time):
        if clock_out_time < self.end_time:
            print('Oops, you cannot clock out before your assigned end time.')
            return
        self.clock_out_time = clock_out_time

    def start_lunch(self, lunch_start_time):
        if self.is_lunch_taken:
            return
        if lunch_start_time < self.start_time:
            print('Oops, You dont have any shift assigned this time.')
            return
        if self.end_time - self.lunch_time < lunch_start_time < self.end_time:
            print('Oops, there is not enough time to start lunch.')
            return
        if lunch_start_time > self.end_time:
            print('Oops, You dont have any shift assigned this time.')
            return
        self.lunch_start_time = lunch_start_time
        self.is_lunch_started = True

    def end_lunch(self, lunch_end_time):
        if not self.is_lunch_started:
            print('Oops, you cannot end your lunch without starting it.')
            return
        if lunch_end_time - self.lunch_start_time < self.lunch_time:
            print('Oops, you cannot end your lunch time early.')
            return
        if lunch_end_time > self.end_time:
            print('Oops, you cannot end your lunch after end time.')
            return
        self.lunch_end_time = lunch_end_time
        self.is_lunch_taken = True