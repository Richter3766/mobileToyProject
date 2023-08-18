import firebase_admin
from firebase_admin import auth, credentials
from flask import Flask
from diningServer.routes import routes_list
from werkzeug.serving import WSGIRequestHandler

WSGIRequestHandler.protocol_version = "HTTP/1.1"


def create_app():
    app = Flask(__name__)

    # routes list
    # from toy.routes import routes_list
    # routes_list(app)

    routes_list(app)

    return app


cred = credentials.RefreshToken('path/to/refreshToken.json')
default_app = firebase_admin.initialize_app(cred)

app1 = create_app()
app1.run('0.0.0.0', port=5000, debug=False)
