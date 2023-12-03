from flask import Blueprint, request, Response, jsonify, json, session
from config import app


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard', methods=['GET'])
def get_dashboard_info():
        #open database connection, and fetch data from database
        cur = app.mysql.connection.cursor()
#         emp_no = session['employee_no']
#         print(emp_no)
        cur.execute("SELECT * FROM salary", (10001,))

        salaries_data = cur.fetchall()
        cur.close()

        # Prepare data for JSON response
        years = [data[0] for data in salaries_data]
        salaries = [data[1] for data in salaries_data]

        return jsonify({'years': years, 'salaries': salaries})
