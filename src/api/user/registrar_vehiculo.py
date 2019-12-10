#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.vehiculo import Vehiculo

INDEX = 'registrar'
PATH = '/ucar/vehiculo/'
index_vehiculo_registrar = Blueprint(PATH + INDEX, __name__)

@index_vehiculo_registrar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def vehiculo_registrar():
    try:
        data = dict(request.get_json())
        query = Vehiculo.select().where(Vehiculo.fkPersona == data['fkPersona']).limit(1)
        if query.exists():
            Vehiculo.update(**data).execute()
        else:
            Vehiculo(**data).save()
        update_user_conn([data['fkPersona']])
        return {'status':'ok', 'message':'Vehiculo registrado'}
    except:
        return {'status':'error', 'message':'Error al guardar'}
    return {'status':'ok', 'message':'Usuario no encontrado'}