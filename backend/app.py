from flask import Flask, \
    render_template, \
    session, \
    Response, \
    jsonify, \
    make_response, \
    request, \
    json
from datetime import timedelta
from config import app, socketio
from routes.auth import auth
from routes.clock import Clock
from routes.pay import Pay
from flask_cors import CORS
from flask_mysqldb import MySQL
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'fang'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'employees'

mysql = MySQL(app)

# Test/sample data table
""" headings = ("Employee No.", "Salary", "Employment Start Date", "Employment End Date") """
""" data = {
    (10001,60117,'1986-06-26','1987-06-26'),
    (10001,62102,'1987-06-26','1988-06-25'),
    (10001,66074,'1988-06-25','1989-06-25'),
    (10001,66596,'1989-06-25','1990-06-25'),
    (10001,66961,'1990-06-25','1991-06-25'),
    (10001,71046,'1991-06-25','1992-06-24'),
    (10001,74333,'1992-06-24','1993-06-24')
} """

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test')
def test():
    output = 'testing'
    return Response(json.dumps(output), status=200)

# authentication routes
@app.route('/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # get user input
        employee_no = request.json['employee_no']
        password = request.json['password']

        #open database connection, and fetch data from database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employees WHERE emp_no = %s AND password = %s", (employee_no, password))
        user = cur.fetchone()
        cur.close()

        # check exist or not, the data fetched from database
        if user:
            # add the user to session
            session['employee_no'] = employee_no
            session['password'] = password
            output = {'employee_no': employee_no}
            res = {'message': 'success', 'error': False, 'output': output}
            #return the user data fetched from database to frontend
            return Response(json.dumps(res), status=200)
        else:
            # return error message to frontend
            return Response(json.dumps({'message': 'Invalid email or password'}), status=401)

@app.route('/auth/signup', methods=['POST'])
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

        return Response(json.dumps({'message': 'User registration successfully'}), status=200)
    
@app.route('/pay_table')
def table():
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM employees.salaries")
    data = cur.fetchall()
    
    headings = [i[0] for i in cur.description]

    return render_template('table.html', headings=headings, data=data)

""" @app.route('/pay')
def getSalary():
    output = 'Welcome employee! This is a test'
    # return Response(json.dumps(output), status=200)
    return Response(json.dumps(output), status=200) """

app.register_blueprint(auth)
app.register_blueprint(Clock)
app.register_blueprint(Pay)

if __name__ == '__main__':
    socketio.run(app, debug=True)
