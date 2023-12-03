from flask import Flask, \
    render_template, \
    session, \
    Response, \
    jsonify, \
    make_response, \
    request, \
    json
from config import app
from routes.auth import auth
from routes.clock import Clock
from routes.Message import socketio, message
from routes.admin_route import admin_route
from models.admin import admin


# authentication routes
app.register_blueprint(auth)
app.register_blueprint(Clock)
app.register_blueprint(message)
app.register_blueprint(admin_route)

if __name__ == '__main__':
    socketio.run(app, debug=True)
