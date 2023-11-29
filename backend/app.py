from flask import Flask, \
    render_template, \
    session, \
    Response, \
    jsonify, \
    make_response, \
    request, \
    json
from config import app, socketio
from routes.auth import auth
from routes.Clock import clock
from routes.pay import Pay

@app.route('/test')
def test():
    output = 'testing'
    return Response(json.dumps(output), status=200)

# authentication routes
app.register_blueprint(auth)
app.register_blueprint(clock)
app.register_blueprint(Pay)

if __name__ == '__main__':
    socketio.run(app, debug=True)
