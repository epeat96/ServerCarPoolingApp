#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import jsonify
from flask import Blueprint
from api.util import require_api_token
from orm.model.ucar.persona import Persona
from peewee import Select
INDEX = 'datos/'
PATH = '/ucar/usuario/'
index_usuario_datos = Blueprint(INDEX, __name__)

@index_usuario_datos.route(PATH + INDEX, methods=['GET'])
@require_api_token
def usuario_datos():
	data = []
	try:
		query = Persona.select().where(Persona.email == request.args.get("email"))
		if query:
			for result in query.dicts():
				data.append(result)
		else:
			return {"status":"error","message":"Esa Persona no existe!"}
	except:
		return {"status":"error","message":"Error de conexion!"}
	return jsonify(data[0])
