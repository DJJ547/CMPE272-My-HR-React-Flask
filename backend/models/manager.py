class Manager:
    def __init__(self, employee_no, first_name, last_name, birthdate, gender, from_date, to_date):
        self.employee_no = employee_no
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.from_date = from_date
        self.to_date = to_date

        
    def assign_shifts(self, employee_id, shift):
        for x in enumerate(self.department_employees):
            if x.employee_no == employee_id:
                x.shifts.append(shift)
                break
        else: 
            print('Employee with that ID was not found under the current Manager');
    
    def look_up_shifts(self, employee_id):
        for x in enumerate(self.department_employees):
            if x.employee_no == employee_id:
                return x.shifts
                break
        else: 
            print('Employee with that ID was not found under the current Manager');