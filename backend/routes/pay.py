from flask import Blueprint, request, Response, jsonify, json
from config import app
from flask_cors import CORS
from flask_mysqldb import MySQL
import os

Pay = Blueprint('Pay', __name__)

""" calc_salary = { "current_salary": 315, "hours": 8 }
monthly_income = {
    "january": 2000,
    "febuary": 1540,
    "march": 5631,
    "april": 4141
} """

@Pay.route('/pay', methods=['GET'])
def getSalary():
    search = app.redis.get('employee_no')

    print(search)

    cur = app.mysql.connection.cursor()

    cur.execute("SELECT salary FROM salaries WHERE emp_no = %s", (search,))
    data = cur.fetchall()
    
    cur.close()

    output = list(data)

    """ print(type(data))
    print(data) """

    return Response(json.dumps(output), status=200)