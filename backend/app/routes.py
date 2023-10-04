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

app = Flask(__name__)

CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test')
def test():
    output = 'testing'
    return Response(json.dumps(output), status=200)