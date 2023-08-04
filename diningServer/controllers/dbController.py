import json

from flask import Blueprint, request

from diningServer.services import dbService
# import toy.services.test_serveice as example_services


db_bp = Blueprint(name='dbRequest',
                  import_name=__name__,
                  url_prefix='/db')


@db_bp.route('/request', methods=['GET'])
def request_route() -> str:
    page = int(request.args.get('page'))
    result = dbService.request(page)
    return json.dumps([{'seq': row[0], 'name': row[1], 'field': row[2], 'address': row[3]} for row in result])
