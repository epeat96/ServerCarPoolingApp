#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import jsonify
from flask import request
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.vehiculo import Vehiculo

INDEX = 'listar/'
PATH = '/ucar/vehiculo/'
index_vehiculo_listar = Blueprint(PATH + INDEX, __name__)

@index_vehiculo_listar.route(PATH + INDEX, methods=['GET'])
@require_api_token
def vehiculo_listar():
	data = []
	try:
		query = Vehiculo.select().where(Vehiculo.fkPersona == request.args.get("id")).limit(1)
		if query.exists():
			for row in query.dicts():
				data.append(row)
			return jsonify(data[0]) 
	except:
		return {"status":"error","message":"Error de conexion!"}
	return {"status":"error","message":"El usuario no existe"}
	