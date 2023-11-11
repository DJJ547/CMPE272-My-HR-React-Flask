from flask import Blueprint, request, Response, jsonify, json
from config import app
from controller.clock import process_punch


Clock = Blueprint('Clock', __name__)

@Clock.route('/dashboard/clock', methods=['POST'])
def clock():
    punch_type = request.json.get('type')
    print(punch_type)
    punch_time = request.json.get('time')
    print(punch_time)
    output = process_punch(punch_type, punch_time)
    return Response(json.dumps(output), status=200)