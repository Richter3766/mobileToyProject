import json

from flask import Blueprint, Response, request
from flask import jsonify

from diningServer.services import AuthService

# import toy.services.test_serveice as example_services


auth_bp = Blueprint(name='auth',
                    import_name=__name__,
                    url_prefix='/auth')


@auth_bp.route('/signIn', methods=['POST'])
def signIn_route() -> str:
    token = str(request.args.get('token'))
    uid = AuthService.verify(token=token)

    custom_token = AuthService.getToken(uid)
    return json.dumps({'result': custom_token})
    # return jsonify(result=result)
