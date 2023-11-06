from flask import Flask, \
    render_template, \
    Response, \
    request, \
    json

from flask_cors import CORS

from controller.clock import process_punch
from models.employee import Employee
app = Flask(__name__)

CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/clock', methods=['POST'])
def clock():
    punch_type = request.json.get('type')
    print(punch_type)
    punch_time = request.json.get('time')
    print(punch_time)
    output = process_punch(punch_type, punch_time)
    return Response(json.dumps(output), status=200)


@app.route('/test')
def test():
    output = 'testing'
    return Response(json.dumps(output), status=200)


if __name__ == '__main__':
    app.run(debug=True)
