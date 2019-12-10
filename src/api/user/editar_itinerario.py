#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.itinerario import Itinerario
from api.util import update_user_conn

INDEX = 'editar'
PATH = '/ucar/itinerario/'
index_editar_itinerario = Blueprint( PATH + INDEX, __name__)

@index_editar_itinerario.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def editar_itinerario():
	try:	
		data = dict(request.get_json())
		new = Itinerario(**data)
		update_user_conn([data['fk_persona']])
		new.save()
		return {"status" : "ok", "message" : "Itinerario Guardado!"}
	except:
		return {"status" : "error", "message" : "No existe el usuario!"}
