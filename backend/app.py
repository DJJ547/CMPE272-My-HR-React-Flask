from flask import Flask, \
    render_template, \
    session, \
    Response, \
    jsonify, \
    make_response, \
    request, \
    json
from datetime import timedelta
from config import app
from routes.auth import auth
import os


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test')
def test():
    output = 'testing'
    return Response(json.dumps(output), status=200)

# authentication routes
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)