from flask import Blueprint, Response
from flask import jsonify

# import toy.services.test_serveice as example_services
from ..services import AuthService

auth_bp = Blueprint(name='auth',
                    import_name=__name__,
                    url_prefix='/auth')


@auth_bp.route('/signup', methods=['POST'])
def example_route() -> Response:
    data = 'hello_world'
    result = AuthService.signup(data=data)
    return jsonify(result=result)


@auth_bp.route('/login', methods=['POST'])
def example_route_add_param(user_number: int) -> Response:
    result = AuthService.login(user_number)
    return jsonify(result=result)
