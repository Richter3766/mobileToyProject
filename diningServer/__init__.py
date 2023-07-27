from flask import Flask


def create_app():
    app = Flask(__name__)

    # routes list
    # from toy.routes import routes_list
    # routes_list(app)
    from routes import routes_list
    routes_list(app)

    return app


app1 = create_app()
app1.run()
