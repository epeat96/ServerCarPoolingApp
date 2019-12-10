#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona
from api.util import update_user_conn
import subprocess as sub
INDEX = 'subir'
PATH = '/foto/'
index_foto_subir = Blueprint( PATH + INDEX, __name__)

@index_foto_subir.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def SubirFoto():
	try:	
		data = dict(request.get_json())
		query = Persona.select().where(Persona.id == data['userId'])
		if query.exists():
			update_user_conn([data['userId']])
			foto = open("/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/aux","w")
			foto.write(data['imgData'])
			foto.close()
			sub.run(["/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/decode.sh","/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/aux","/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/" + str(data['userId'])])
			sub.run(["/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/rename.sh","/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/" + str(data['userId'])])
			return {"status" : "ok", "message" : "Foto Subida!"}
		else:	
			return {"status" : "error", "message" : "Esa persona no existe!"}
	except:
		return {"status" : "error", "message" : "Error Interno"}
