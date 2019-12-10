#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.viaje_reservado import ViajeReservado
INDEX = 'cancelar/'
PATH = '/ucar/viaje/'
index_reserva_cancelar = Blueprint(INDEX, __name__)

@index_reserva_cancelar.route(PATH + INDEX, methods=['GET'])
@require_api_token
def viaje_reservar():
	try:	
		if  ViajeReservado.delete().where(ViajeReservado.id == request.args.get("id_viaje") ).execute():
			return { "status" : "ok", "message" : "Viaje Cancelado!"}
		else :
			return { "status" : "error", "message" : "El viaje no existe!"}
	except:
		return { "status" : "error", "message" : "Bad Request!"}
