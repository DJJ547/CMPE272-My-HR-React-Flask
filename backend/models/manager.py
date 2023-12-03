from models.employee import Employee
from config import app
from utils import date_convertor, shifts_db
from datetime import datetime

class Manager(Employee):
    def __init__(self, employee_no):
        super().__init__(employee_no)
        self.dept_no = app.redis.get('dept_no')
        self.from_date = app.redis.get('from_date')
        self.to_date = app.redis.get('to_date')
    
    # get all info for employees in this apartment, make sure their "to_date" is "9999-01-01", meaning they are currently still working
    def get_department_employees(self):
        cur = app.mysql.connection.cursor()
        cur.execute("SELECT * FROM dept_emp INNER JOIN employees ON dept_emp.emp_no = employees.emp_no WHERE dept_no = %s AND to_date = %s", (self.dept_no, datetime(9999, 1, 1)))
        db_dept_employees = cur.fetchall()
        cur.close()
        return db_dept_employees
    
    def get_dept_emp_shifts(self, emp_no):
        dept_emp_shifts = shifts_db.get_shifts_from_db(emp_no)
            