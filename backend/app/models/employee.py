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

    def start_shift(self, clock_in_time):
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_actual_start_time_on_time(clock_in_time):
                shift.set_actual_start_time(clock_in_time)
                print("Congratulation, you clocked in on time.")
                return
            if shift.check_actual_start_time_late(clock_in_time):
                shift.set_actual_start_time(clock_in_time)
                shift.is_late = True
                print("Oops, you clocked in late")
                return
        print("Oops, You dont have any shift assigned this time.")

    def end_shift(self, clock_out_time):
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_actual_end_time(clock_out_time):
                shift.set_actual_end_time(clock_out_time)
                return
        print("Oops, You dont have any shift started.")

    def start_lunch(self, lunch_start_time):
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_actual_lunch_start_time(lunch_start_time):
                shift.set_actual_lunch_start_time(lunch_start_time)
                return
        print("Oops, you don't have any started shift that requires a lunch break.")

    def end_lunch(self, lunch_end_time):
        # loop thru each shift and find the current one
        for shift in self.shifts:
            if shift.check_actual_lunch_end_time(lunch_end_time):
                shift.set_actual_lunch_end_time(lunch_end_time)
                return
        print("Oops, you don't have any lunch started.")
