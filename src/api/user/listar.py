#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import jsonify
from flask import Blueprint
from api.util import require_api_token
from orm.model.ucar.persona import Persona

INDEX = 'listar/'
PATH = '/ucar/usuario/'
index_usuario_listar = Blueprint(INDEX, __name__)

@index_usuario_listar.route(PATH + INDEX, methods=['GET'])
@require_api_token
def usuario_listar():
    data = []
    try:
        query = Persona.select()
        for result in query.dicts():
            data.append(result)
    except:
        return {"status":"error","message":"Error de conexion!"}
    return jsonify(data)
