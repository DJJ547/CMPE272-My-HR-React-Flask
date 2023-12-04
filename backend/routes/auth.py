from flask import Blueprint, request, Response, jsonify, json, session
import jwt
from config import app
from models.employee import Employee
from models.manager import Manager
from models.admin import Admin
from utils import date_convertor
# authentication routes
from models.admin import admin
auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # get user input
        employee_no = request.json['employee_no']
        password = request.json['password']

        # open database connection, and fetch data from database
        cur = app.mysql.connection.cursor()
        cur.execute("SELECT * FROM employees WHERE emp_no = %s AND password = %s", (employee_no, password))
        user_info = cur.fetchone()
        cur.close()

        # check exist or not, the data fetched from database
        if user_info:
            # add jwt token
            token = jwt.encode({'employee_no': employee_no},
                               app.secret_key, algorithm='HS256')

            employee_no = user_info[0]
            birthdate = user_info[1]
            first_name = user_info[2]
            last_name = user_info[3]
            gender = user_info[4]
            hire_date = user_info[5]

            cur = app.mysql.connection.cursor()
            cur.execute("SELECT * FROM dept_emp WHERE emp_no = %s", (employee_no,))
            dept_info = cur.fetchone()
            dept_no = dept_info[1]
            from_date = dept_info[2]
            to_date = dept_info[3]

            # load data into redis server side session
            app.redis.set('employee_no', employee_no)
            app.redis.set('first_name', first_name)
            app.redis.set('last_name', last_name)
            app.redis.set('birthdate', date_convertor.convert_datetime_to_string(birthdate))
            app.redis.set('gender', gender)
            app.redis.set('hire_date', date_convertor.convert_datetime_to_string(hire_date))
            app.redis.set('dept_no', dept_no)
            app.redis.set('from_date', date_convertor.convert_datetime_to_string(from_date))
            app.redis.set('to_date', date_convertor.convert_datetime_to_string(to_date))

            # check if he is a manager
            cur.execute("SELECT * FROM dept_manager WHERE emp_no = %s", (employee_no,))
            manager_info = cur.fetchone()
            cur.close()
            state = None
            if manager_info:
                state = 'M'
                dept_no = manager_info[1]
                from_date = manager_info[2]
                to_date = manager_info[3]
                # manager = Manager(employee_no, first_name, last_name, birthdate, gender, hire_date,  dept_no, from_date, to_date)
                app.redis.set('state', state)
            else:
                state = 'E'
                # employee = Employee(employee_no, birthdate, first_name, last_name, gender, hire_date)
                app.redis.set('state', state)

            data = {'employee_no': employee_no, 'first_name': first_name, 'last_name': last_name, 'hire_date': hire_date, 'birthdate': birthdate, 'gender': gender, 'dept_no': dept_no, 'from_date': from_date, 'to_date': to_date, 'state': state}
            
            response = {'message': 'success', 'error': False, 'data': data, 'token': token}
            #return the user data fetched from database to frontend
            return Response(json.dumps(response), status=200)
        else:
            cur.close()
            # return error message to frontend
            return Response(json.dumps({'message': 'Invalid email or password'}), status=401)
        
@auth.route('/auth/logout', methods=['GET'])
def logout():
    if request.method == 'GET':
        app.redis.flushall()
    return Response(json.dumps({'message': 'Successfully logged out'}), status=200)

""" 
@auth.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        name = request.json['name']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        existingUser = cur.fetchone()

        if existingUser:
            cur.close()
            return jsonify({'message': 'email already registered'})
        else:
            cur.execute("INSERT INTO users (email, password, name) VALUES (%s, %s, %s)", (email, password, name))
            mysql.connection.commit()
            cur.close()

        return Response(json.dumps({'message': 'User registration successfully'}), status=200) """
