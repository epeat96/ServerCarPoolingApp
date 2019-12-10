#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
#from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona

INDEX = 'actualizar'
PATH = '/ucar/perfil/'
index_perfil_actualizar = Blueprint(INDEX, __name__)

@index_perfil_actualizar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def actualizar_perfil():
	try:
		data = dict(request.get_json())
		query = Persona.select().where(Persona.id == data['id'])
		if query.exists():
			#update_user_conn([data['userId']])
			if data['password'] == "":
				nrows = (Persona.update(
						nombre=data['nombre'],
						apellido=data['apellido'],
						email=data['email'],
						institucion=data['institucion']).where(Persona.id == data['id']).execute())
			else:			
				nrows = (Persona.update(
						nombre=data['nombre'],
						apellido=data['apellido'],
						email=data['email'],
						institucion=data['institucion'],
						password=data['password']).where(Persona.id == data['id']).execute())	
			#update_user_conn([data['id']])
			return {"status":"ok","message":"Perfil Modificado!"}
		return {'status':'error', 'message':'Esa persona no existe!'}
	except:
		return {'status':'error','message':'Error de conexion!'}
