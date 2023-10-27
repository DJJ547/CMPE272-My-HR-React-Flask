import datetime
from datetime import timedelta

from employee import Employee


class Shift:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        # assign default time
        self.clock_in_time = datetime.datetime(2000, 1, 1, 1, 1)
        self.clock_out_time = datetime.datetime(2000, 1, 1, 1, 1)
        self.lunch_start_time = datetime.datetime(2000, 1, 1, 1, 1)
        self.lunch_end_time = datetime.datetime(2000, 1, 1, 1, 1)
        self.lunch_time = self.calculate_lunch_time()
        self.check_if_late = False
        self.is_lunch_taken = False
        self.is_lunch_started = False

    def calculate_lunch_time(self):
        lunch_time = timedelta(hours=0)
        if self.end_time - self.start_time >= timedelta(hours=8):
            lunch_time = timedelta(hours=1)
        elif timedelta(hours=4) <= self.end_time - self.start_time <= timedelta(hours=8):
            lunch_time = timedelta(hours=0.5)
        return lunch_time

    def set_lunch_taken(self):
        if not self.is_lunch_taken:
            self.is_lunch_taken = True

    # if clock out time minus clock in time larger than or equal to end_time minus start time
    def check_if_shift_complete(self):
        # if employee clock out before or number of hours work less than assigned amount
        if self.end_time < self.clock_out_time and self.clock_out_time - self.clock_in_time >= self.end_time - self.start_time:
            return False
        return True

    def start_shift(self, clock_in_time):
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


def main():
    first_shift = datetime.datetime(2023, 9, 29, 24, 23)
    shifts = [first_shift]
    em = Employee(1, 'Jiajun', 'Dai', datetime.datetime(1995, 4, 20), 'M', datetime.datetime(2023, 9, 10), shifts)


    # Attributes: hour, minute, second, microsecond, and tzinfo.
    # assigned_shift_start_time = datetime.datetime(2023, 9, 29, 12, 0)
    # assigned_shift_end_time = datetime.datetime(2023, 9, 28, 14, 0)
    # clock_in_time = datetime.datetime(2023, 9, 29, 12, 0)
    # print(f'actual clock in time: {clock_in_time}')
    # clock_out_time = datetime.datetime.today()
    # print(f'actual clock out time: {clock_out_time}')
    # shift1 = Shift()


if __name__ == '__main__':
    main()
