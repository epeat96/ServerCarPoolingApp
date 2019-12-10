#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from peewee import Select
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona

INDEX = 'identificar'
PATH = '/ucar/usuario/'
index_usuario_identificar = Blueprint(INDEX, __name__)

@index_usuario_identificar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def usuario_identificar():
	query = Select(None)
	try:
		data = dict(request.get_json())
		query = Persona.select(Persona.id, Persona.email, Persona.password)\
			.where((Persona.email == data['email']) & (Persona.password == data['password']))
		if query.exists():
			update_user_conn([query[0].id])
			return {'status':'ok','message': f'{query[0].id}'}
	except:
		return {"status":"error","message":"pg select"}
	return {'status':'error','message':'El usuario no se encuentra registrado!'}
