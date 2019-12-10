#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona
from orm.model.client.cliente import Cliente

INDEX = 'registrar'
PATH = '/ucar/usuario/'
index_usuario_registrar = Blueprint(INDEX, __name__)

@index_usuario_registrar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def usuario_registrar():
	try:
		data = dict(request.get_json())
		query = Cliente.select().where(Cliente.email == data['email'])
		if query.exists():
			new = Persona(**data)
			new.save()
			return {"status":"ok","message":"usuario creado"}
		return {'status':'error', 'message':'Email no admitido!'}
	except:
		return {'status':'error','message':'Error de conexion!'}
	return {'status':'error','message':'usuario no creado'}
