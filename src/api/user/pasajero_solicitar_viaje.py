#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
import datetime
from datetime import date
from orm.model.ucar.cola_de_pedidos import ColaDePedidos
INDEX = 'solicitar'
PATH = '/ucar/pasajero/viaje/'
index_pasajero_solicitar_viaje = Blueprint(PATH + INDEX, __name__)

@index_pasajero_solicitar_viaje.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def PasajeroSolicitarViaje():
	try:    
		data = dict(request.get_json())
		query = ColaDePedidos.select().where((ColaDePedidos.fk_persona_id==data["fk_persona_id"]) & (ColaDePedidos.estado=="no atendido") )
		if query.exists() :
			return {"status" : "error", "message" :"Ya tiene un pedido de viaje!"}
		else :
			data["fecha"] = date.today().strftime("%d/%m/%Y")
			data["hora"] = datetime.datetime.now()
			data["estado"] = "no atendido"
			new = ColaDePedidos(**data)
			new.save()
			return {"status" : "ok", "message" : "Solicitud Agregada a la cola!"}
	except:
		return {"status" : "error", "message" : "No existe el usuario!"}
