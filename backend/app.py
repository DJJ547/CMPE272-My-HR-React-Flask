from flask import Flask, \
    render_template, \
    session, \
    Response, \
    jsonify, \
    make_response, \
    request, \
    json
from datetime import timedelta
from flask_cors import CORS
from flask_mysqldb import MySQL
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fang'
app.config['MYSQL_DB'] = 'employees'

mysql = MySQL(app)

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
        email = request.json['email']
        password = request.json['password']

        #open database connection, and fetch data from database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()

        # check exist or not, the data fetched from database
        if user:
            # add the user to cookie
            session['email'] = email
            session['password'] = password
            #return the user data fetched from database to frontend
            return Response(json.dumps({'message': 'success', 'user':user }), status=200)
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

if __name__ == '__main__':
    app.run(debug=True)