from re import search
from uuid import uuid1
from hashlib import md5
from flask import request
from flask import Blueprint
from api.util import ucar_sendemail
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona

INDEX = 'recuperar/'
PATH = '/ucar/usuario/'
index_recuperar_cuenta = Blueprint(INDEX, __name__)

@require_api_token
@content_type_json
@index_recuperar_cuenta.route(PATH + INDEX, methods=['GET'])
def usuario_recuperar_cuenta():
    data = request.args.get('email')
    if data:
        query = Persona.select(Persona.password).where(Persona.email == data)
        if query.exists():
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if search(regex, data):
                pw = str(uuid1())[0:5]
                query = (Persona.update({Persona.password: md5(pw.encode()).hexdigest()}).where(Persona.email == data).execute())
                if query:
                    ucar_sendemail(data, f'password {pw}')
                    return {'status':'ok', 'message' : 'email enviado'}
                return {'status':'error', 'message' : 'error al actualizar'}
            return {'status':'error', 'message' : 'email no valido'}
        return {'status':'error', 'message' : 'email no encontrado'}
    return {'status':'error', 'message' : 'falta parametro'}