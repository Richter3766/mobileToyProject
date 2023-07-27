from controllers.AuthController import auth_bp


def routes_list(app):
    app.register_blueprint(auth_bp)
    return app
