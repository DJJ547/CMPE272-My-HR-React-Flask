from flask import Blueprint, request, Response, jsonify, json
from config import app
from flask_cors import CORS
from flask_mysqldb import MySQL
import os

Pay = Blueprint('Pay', __name__)

@Pay.route('/pay', methods=['GET'])
def getSalary():
    cur = app.mysql.connection.cursor()

    cur.execute("SELECT salary FROM salaries WHERE emp_no = %s", (10001,))
    data = cur.fetchall()
    
    cur.close()

    output = data
    return Response(json.dumps(output), status=200)