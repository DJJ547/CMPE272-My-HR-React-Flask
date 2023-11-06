import datetime
from datetime import timedelta

from models.employee import Employee


class Shift:
    def __init__(self, assigned_start_time, assigned_end_time):
        self.assigned_start_time = assigned_start_time
        self.assigned_end_time = assigned_end_time
        self.actual_start_time = None
        self.actual_end_time = None
        # lunch start and end time will be calculated at the time of initiating a shift
        self.assigned_lunch_start_time = self.calculate_lunch_start_time()
        self.assigned_lunch_end_time = self.calculate_lunch_end_time()
        self.lunch_duration = self.calculate_lunch_duration()
        self.actual_lunch_start_time = None
        self.actual_lunch_end_time = None

        self.is_late = False
        # status are either new, started, or ended
        self.shift_status = 'new'
        self.lunch_status = 'new'

    def calculate_lunch_start_time(self):
        lunch_start_time = None
        # lunchtime will be every four hours
        if self.assigned_end_time - self.assigned_start_time > timedelta(hours=4):
            lunch_start_time = self.assigned_start_time + timedelta(hours=4)
        return lunch_start_time

    def calculate_lunch_end_time(self):
        lunch_end_time = None
        if self.assigned_lunch_start_time is not None:
            # lunchtime will be every four hours
            if self.assigned_end_time - self.assigned_start_time >= timedelta(hours=8):
                lunch_end_time = self.assigned_lunch_start_time + timedelta(hours=1)
            elif timedelta(hours=4) < self.assigned_end_time - self.assigned_start_time < timedelta(hours=8):
                lunch_end_time = self.assigned_lunch_start_time + timedelta(hours=0.5)
        return lunch_end_time

    def calculate_lunch_duration(self):
        lunch_duration = timedelta(0)
        if self.assigned_end_time - self.assigned_start_time >= timedelta(hours=8):
            lunch_duration = timedelta(hours=1)
        elif timedelta(hours=4) < self.assigned_end_time - self.assigned_start_time < timedelta(hours=8):
            lunch_duration = timedelta(minutes=30)
        return lunch_duration

    def check_actual_start_time_on_time(self, clock_in_time):
        if self.shift_status == 'new' and -timedelta(
                minutes=5) <= clock_in_time - self.assigned_start_time <= timedelta(minutes=5):
            return True
        return False

    def check_actual_start_time_late(self, clock_in_time):
        if self.shift_status == 'new' and timedelta(minutes=5) < clock_in_time - self.assigned_start_time <= timedelta(
                minutes=30):
            return True
        return False

    def check_actual_end_time(self, clock_out_time):
        if self.shift_status == 'started' and -timedelta(
                minutes=5) <= clock_out_time - self.assigned_end_time <= timedelta(minutes=10):
            return True
        return False

    def set_actual_start_time(self, clock_in_time):
        self.actual_start_time = clock_in_time
        self.shift_status = 'started'

    def set_actual_end_time(self, clock_out_time):
        self.actual_end_time = clock_out_time
        self.shift_status = 'ended'

    def check_actual_lunch_start_time(self, lunch_start_time):
        if self.lunch_status == 'new' and self.assigned_lunch_start_time <= lunch_start_time <= self.assigned_end_time - self.lunch_duration:
            return True
        return False

    def check_actual_lunch_end_time(self, lunch_end_time):
        if self.lunch_status == 'started' and lunch_end_time - self.assigned_lunch_start_time >= self.lunch_duration and lunch_end_time <= self.assigned_end_time - self.lunch_duration:
            return True
        return False

    def set_actual_lunch_start_time(self, lunch_start_time):
        self.actual_lunch_start_time = lunch_start_time
        self.lunch_status = 'started'

    def set_actual_lunch_end_time(self, lunch_end_time):
        self.actual_lunch_end_time = lunch_end_time
        self.lunch_status = 'ended'

    def check_is_shift_ended(self):
        if self.shift_status == 'ended':
            return True
        return False

    def print_all_shift_info(self):
        print(self.__dict__)
