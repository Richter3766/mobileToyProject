from diningServer.controllers.AuthController import auth_bp
from diningServer.controllers.dbController import db_bp


def routes_list(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(db_bp)
    return app
