import json

from flask import Blueprint, Response
from flask import jsonify

from diningServer.services import dbService

# import toy.services.test_serveice as example_services


db_bp = Blueprint(name='dbRequest',
                  import_name=__name__,
                  url_prefix='/db')


@db_bp.route('/request', methods=['GET'])
def request_route() -> str:
    result = dbService.request()
    return json.dumps(result, indent=4)
