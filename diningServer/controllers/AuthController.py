import json

from flask import Blueprint, Response, request
from flask import jsonify

from diningServer.services import AuthService

# import toy.services.test_serveice as example_services


auth_bp = Blueprint(name='auth',
                    import_name=__name__,
                    url_prefix='/auth')


@auth_bp.route('/verify', methods=['POST'])
def verify_route() -> str:
    token = str(request.args.get('token'))
    result = AuthService.verify(token=token)
    return json.dumps({'result': result})
    # return jsonify(result=result)


@auth_bp.route('/login', methods=['POST'])
def example_route_add_param(user_number: int) -> Response:
    result = AuthService.login(user_number)
    return jsonify(result=result)
