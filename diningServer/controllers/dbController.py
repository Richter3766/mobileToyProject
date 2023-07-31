from flask import Blueprint, Response
from flask import jsonify

from diningServer.services import AuthService, dbService

# import toy.services.test_serveice as example_services


auth_bp = Blueprint(name='dbRequest',
                    import_name=__name__,
                    url_prefix='/db')


@auth_bp.route('/request', methods=['GET'])
def example_route() -> Response:
    data = 'hello_world'
    result = dbService.request(data=data)
    return jsonify(result=result)
