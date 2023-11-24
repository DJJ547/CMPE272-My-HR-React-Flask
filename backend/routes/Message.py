from flask import Blueprint, request, Response, jsonify, json
import jwt
from flask_socketio import SocketIO
from config import app
from socketio_init import socketio


@socketio.on('connect')
def connect():
    print('connected')

""" @socketio.on('message')
def handle_message(data):
    # Save message to MySQL database
    cur = app.mysql.connection.cursor()
    cur.execute("INSERT INTO chat_history (sender, receiver, message) VALUES (%s, %s, %s)",
                (data['sender'], data['receiver'], data['message']))
    app.mysql.connection.commit()
    cur.close()

    # Broadcast message to all connected clients
    socketio.emit('message', data) """
