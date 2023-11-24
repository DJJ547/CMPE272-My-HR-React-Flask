from flask import Flask, Blueprint, request, Response, jsonify, json
from flask_cors import CORS
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="http://localhost:3000")
