from flask import Flask, Blueprint, request, Response, jsonify, json
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_socketio import SocketIO
from routes.Message import socketio
import redis
import os
import sys

#app configuration
class MyApp(Flask):
    def __init__(self, import_name):
        super(MyApp, self).__init__(import_name)
        self.secret_key = os.urandom(24)
        self.config['MYSQL_HOST'] = 'localhost'
        self.config['MYSQL_USER'] = 'root'
        #self.config['MYSQL_PASSWORD'] = 'fang'
        self.config['MYSQL_PASSWORD'] = 'password'
        self.config['MYSQL_DB'] = 'employees'
        self.mysql = MySQL(self)
        socketio.init_app(self)
        CORS(self)
        self.redis = redis.Redis(host='localhost', port=6379, decode_responses=True)



app = MyApp(__name__)