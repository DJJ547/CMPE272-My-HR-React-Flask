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
from routes.Clock import clock
from routes.Message import socketio, message
from routes.admin_route import admin_route
from routes.dashboard import dashboard
from routes.setting import setting
from routes.Schedule import schedule
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
import ssl
import os 

# authentication routes
app.register_blueprint(auth)
app.register_blueprint(clock)
app.register_blueprint(message)
app.register_blueprint(admin_route)
app.register_blueprint(dashboard)
# app.register_blueprint(infoCard)
app.register_blueprint(setting)
app.register_blueprint(schedule)

AUTH0_DOMAIN = "dev-8e5yx4hque4cspbf.us.auth0.com"
AUTH0_CLIENT_ID = "UfmSHzml95JMgG9zcyqmyR2jqNWYI3Pe"
AUTH0_CLIENT_SECRET = "BSSjzWAWq5TxoB0-IaeCaUkbvI268CcZKbhJuz68G0IfCStj7IlEcH38kdj0Lq8x"

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{AUTH0_DOMAIN}/.well-known/openid-configuration'
)

@app.route('/test')
def test():
    output = 'testing'
    return Response(json.dumps(output), status=200)


if __name__ == '__main__':
    socketio.run(app, debug=True)
