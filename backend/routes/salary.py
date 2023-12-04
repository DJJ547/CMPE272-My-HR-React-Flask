from flask import Blueprint, request, Response, jsonify, json, session
from config import app


salary = Blueprint('salary', __name__)

@salary.route('/dashboard/salary', methods=['GET'])
def salaryGraph():
        #open database connection, and fetch data from database
        cur = app.mysql.connection.cursor()
        employee_no = app.redis.get('employee_no')
        cur.execute("SELECT DATE_FORMAT(from_date, '%%Y') as year, salary FROM salaries WHERE emp_no = %s", (employee_no,))

        salaries_data = cur.fetchall()
        cur.close()

        # Prepare data for JSON response
        years = [data[0] for data in salaries_data]
        salaries = [data[1] for data in salaries_data]

        return jsonify({'years': years, 'salaries': salaries})
