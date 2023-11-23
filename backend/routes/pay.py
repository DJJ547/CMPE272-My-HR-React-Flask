from flask import Blueprint, request, Response, jsonify, json
from config import app
from flask_cors import CORS
from flask_mysqldb import MySQL
import os

Pay = Blueprint('Pay}', __name__)

@auth.route('/dashboard/pay', methods=['POST'])
def getSalary():
    output = 'Welcome employee! This is a test'
    return Response(json.dumps(output), status=200)