#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from sys import argv
from flask import Flask
from orm.create.ucar import create_tables
from api.user.registrar import index_usuario_registrar
from api.user.identificar import index_usuario_identificar
from api.user.listar import index_usuario_listar
from api.user.crear_reserva import index_reserva_reservar
from api.user.eliminar_reserva import index_reserva_cancelar
from api.user.listar_reservas import index_reserva_listar
from api.user.subir_foto import index_foto_subir
from api.user.get_user_by_email import index_usuario_datos
from api.user.recuperar_cuenta import index_recuperar_cuenta
from api.user.actualizar_perfil import index_perfil_actualizar
from api.user.registrar_vehiculo import index_vehiculo_registrar
from api.user.editar_itinerario import index_editar_itinerario 
from api.user.pasajero_solicitar_viaje import index_pasajero_solicitar_viaje
from api.user.pasajero_verificar_viaje import index_pasajero_verificar_viaje
from api.user.listar_vehiculo import index_vehiculo_listar
from api.user.conductor_viajes import index_conductor_listar_viajes
#from orm.model.ucar.itinerario import Itinerario

app = Flask(__name__)
app.register_blueprint(index_usuario_registrar)
app.register_blueprint(index_usuario_identificar)
app.register_blueprint(index_usuario_listar)
app.register_blueprint(index_reserva_reservar)
app.register_blueprint(index_reserva_cancelar)
app.register_blueprint(index_reserva_listar)
app.register_blueprint(index_foto_subir)
app.register_blueprint(index_usuario_datos)
app.register_blueprint(index_recuperar_cuenta)
app.register_blueprint(index_perfil_actualizar)
app.register_blueprint(index_vehiculo_registrar)
app.register_blueprint(index_editar_itinerario)
app.register_blueprint(index_pasajero_solicitar_viaje)
app.register_blueprint(index_pasajero_verificar_viaje)
app.register_blueprint(index_vehiculo_listar)
app.register_blueprint(index_conductor_listar_viajes)

if __name__ == '__main__':
    if len(argv) == 2:
        if argv[1] == '--init-db':
            create_tables()

    '''
    new = Itinerario()
    new.latitudOrig = '-57.647976859562334'
    new.longitudOrig = '-25.285515826523806'
    new.latitudDst = '-57.63543469077945'
    new.longitudDst  = '-25.324514646565376'
    new.dia = 'lunes'
    new.fecha = '10-12-2019'
    new.horaEntrada = '10:01'
    new.horaSalida = '12:01'
    new.fk_persona = '2'
    new.save()
    '''
    
    app.run()
