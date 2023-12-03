from flask import Blueprint, request, Response, jsonify, json
import jwt
from config import app
# authentication routes
from models.admin import admin
auth = Blueprint('auth', __name__)

@auth.route('/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # get user input
        employee_no = request.json['employee_no']
        password = request.json['password']

        #open database connection, and fetch data from database
        cur = app.mysql.connection.cursor()
        cur.execute("SELECT * FROM employees WHERE emp_no = %s AND password = %s", (employee_no, password))
        user = cur.fetchone()
        cur.close()

        # check exist or not, the data fetched from database
        if user:
            # add jwt token
            token = jwt.encode({'employee_no': employee_no}, app.secret_key, algorithm='HS256')
            
            full_name = user[2] + ' ' + user[3]
            hire_date = user[5]
            birth_date = user[1]
            employee_no = user[0]
            data = {'employee_no': employee_no, 'full_name': full_name, 'hire_date': hire_date, 'birth_date': birth_date}
            
            response = {'message': 'success', 'error': False, 'data': data, 'token': token}
            #return the user data fetched from database to frontend
            return Response(json.dumps(response), status=200)
        else:
            # return error message to frontend
            return Response(json.dumps({'message': 'Invalid email or password'}), status=401)
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
