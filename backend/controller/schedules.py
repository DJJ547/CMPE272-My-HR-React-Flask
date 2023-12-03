from models.employee import Employee
from models.manager import Manager
from models.shift import Shift
from flask import json, session
import datetime
from utils import shifts_db
from config import app

# maybe do this with a SQL join table???
def get_all_dept_employees_and_shifts():
    manager = Manager(app.redis.get('emp_no'))
    dept_emps = manager.get_department_employees()
    # get a list of all department employees id
    dept_emps_nums = []
    for dept_emp in dept_emps:
        dept_emps_nums.append(dept_emp[0])
    # print("dept_emps_nums: ", dept_emps_nums)

    # use a dictionary to store all shifts as value and emp_no as key
    dept_emps_dict = {}
    for num in dept_emps_nums:
        shifts = shifts_db.get_shifts_from_db(num)
        dept_emps_dict[num] = shifts
    print(dept_emps_dict)
    return dept_emps_dict

def get_self_schedule():
    emp_no = app.redis.get('emp_no')
    shifts = shifts_db.get_shifts_from_db(emp_no)
    return shifts