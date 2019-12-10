#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.viaje_reservado import ViajeReservado
from orm.model.ucar.persona import Persona
from api.util import update_user_conn

INDEX = 'reservar'
PATH = '/ucar/reserva/'
index_reserva_reservar = Blueprint(INDEX, __name__)

@index_reserva_reservar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def viaje_reservar():
	try:	
		data = dict(request.get_json())
		new = ViajeReservado(**data)
		update_user_conn([data['fk_persona_id']])
		new.save()
		return {"status" : "ok", "message" : "Viaje Reservado!"}
	except:
		return {"status" : "error", "message" : "No existe el usuario!"}
