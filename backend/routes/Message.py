from flask import Blueprint, request, Response, jsonify, json
import jwt
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="http://localhost:3000")

@socketio.on('connect')
def connect():
    print( 'connected')
