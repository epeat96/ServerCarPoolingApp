#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import jsonify
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.viaje_reservado import ViajeReservado

INDEX = 'listar/'
PATH = '/ucar/reserva/'
index_reserva_listar = Blueprint(PATH + INDEX, __name__)

@index_reserva_listar.route(PATH + INDEX, methods=['GET'])
@require_api_token
def reserva_listar():
	try:	
		respuesta = []
		query = ViajeReservado.select(ViajeReservado.id)	
		for result in query.dicts():
			respuesta.append(result)
		return jsonify(respuesta)
	except:
		return {"status" : "error", "message" : "Error de conexion!"}
