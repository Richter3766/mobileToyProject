from flask import Blueprint, Response
from flask import jsonify

from diningServer.services import AuthService

# import toy.services.test_serveice as example_services


auth_bp = Blueprint(name='auth',
                    import_name=__name__,
                    url_prefix='/auth')


@auth_bp.route('/', methods=['POST'])
def example_route(token: str) -> Response:
    result = AuthService.signup(data=token)
    return jsonify(result=result)


@auth_bp.route('/login', methods=['POST'])
def example_route_add_param(user_number: int) -> Response:
    result = AuthService.login(user_number)
    return jsonify(result=result)
