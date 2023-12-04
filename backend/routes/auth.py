from flask import Blueprint, request, Response, jsonify, json, session
import jwt
from config import app
from models.employee import Employee
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
        cur.execute("""
                          SELECT
                              e.emp_no,
                              e.birth_date,
                              e.first_name,
                              e.last_name,
                              e.gender,
                              e.hire_date,
                              e.profile_pic,
                              e.motto,
                              e.password,
                              d.dept_name,
                              t.title
                          FROM
                              employees e
                          INNER JOIN
                              dept_emp de ON e.emp_no = de.emp_no
                          INNER JOIN
                              departments d ON de.dept_no = d.dept_no
                          INNER JOIN
                              titles t ON e.emp_no = t.emp_no
                          WHERE
                              e.emp_no = %s
                              AND e.password = %s
                              AND de.to_date = (SELECT MAX(de2.to_date) FROM dept_emp de2 WHERE de2.emp_no = e.emp_no)
                              AND t.to_date = (SELECT MAX(t2.to_date) FROM titles t2 WHERE t2.emp_no = e.emp_no)
                          """, (employee_no, password))
        user = cur.fetchone()
        cur.close()

        # check exist or not, the data fetched from database
        if user:
            # add jwt token
            token = jwt.encode({'employee_no': employee_no},
                               app.secret_key, algorithm='HS256')

            full_name = user[2] + ' ' + user[3]
            hire_date = user[5]
            birth_date = user[1]
            employee_no = user[0]
            is_manager = admin.is_manager(employee_no)
            
            #return the user data fetched from database to frontend
            profile_pic = user[6]
            motto = user[7]
            dept_name = user[9]
            title = user[10]

            app.redis.set('employee_no', employee_no)

            data = {'employee_no': employee_no, 'full_name': full_name, 'hire_date': hire_date, 'birth_date': birth_date,
                    'profile_pic': profile_pic, 'motto': motto, 'dept_name': dept_name, 'title': title, 'is_manager': is_manager}

            response = {'message': 'success',
                        'error': False, 'data': data, 'token': token}
            # return the user data fetched from database to frontend
            return Response(json.dumps(response), status=200)
        else:
            # return error message to frontend
            return Response(json.dumps({'message': 'Invalid email or password'}), status=401)
    

@auth.route('/auth/changePassword', methods=['POST'])
def change_password():
    emp_no = request.json['emp_no']
    old_password = request.json['currentPassword']
    new_password = request.json['newPassword']
    
    cur = app.mysql.connection.cursor()
    cur.execute("SELECT * FROM employees WHERE emp_no = %s AND password = %s", (emp_no, old_password))
    user = cur.fetchone()
    if user:
        cur = app.mysql.connection.cursor()
        cur.execute("UPDATE employees SET password = %s WHERE emp_no = %s", (new_password, emp_no))
        app.mysql.connection.commit()
        cur.close()
        return Response(json.dumps({'message': 'Password changed successfully'}), status=200)
    else:
        return Response(json.dumps({'message': 'Invalid current password'}), status=401)



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
