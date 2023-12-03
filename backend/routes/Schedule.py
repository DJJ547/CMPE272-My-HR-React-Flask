from flask import Blueprint, request, Response, jsonify, json, session
from config import app
from controller import schedules

schedule = Blueprint('schedule', __name__)

@schedule.route('/dashboard/manager/schedule', methods=['POST'])
def get_employee_schedules():
    output = schedules.get_all_dept_employees_and_shifts()
    return Response(json.dumps(output), status=200)


@schedule.route('/dashboard/employee/schedule', methods=['GET'])
def get_schedule():
    output = schedules.get_self_schedule()
    return Response(json.dumps(output), status=200)