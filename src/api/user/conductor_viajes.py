#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from flask import jsonify
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.match import Match

INDEX = 'listar'
PATH = '/ucar/conductor/pedidos/'
index_conductor_listar_viajes = Blueprint(PATH + INDEX, __name__)

@index_conductor_listar_viajes.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def conductor_listar_viajes():
	try:
		data = dict(request.get_json())
		query = Match.select().where((Match.fk_chofer == data['fk_chofer']) & (Match.estado == 'no atentido')).limit(1)
		if query.exists():
			return jsonify(query[0])
	except:
		return {'status':'error', 'message':'error de conexion'}
	return {'status':'error', 'message':'usuario no encontrado'}