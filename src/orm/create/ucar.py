#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from orm.conn.db import pg_conn
from orm.model.ucar.persona import Persona
from orm.model.client.cliente import Cliente
from orm.model.ucar.vehiculo import Vehiculo
from orm.model.ucar.itinerario import Itinerario
from orm.model.ucar.viaje_reservado import ViajeReservado
from orm.model.ucar.viaje import Viaje
from orm.model.ucar.cola_de_pedidos import ColaDePedidos
from orm.model.ucar.match import Match

def create_tables():
    TABLES = [Persona, Cliente, ViajeReservado, Vehiculo, Itinerario, Viaje, ColaDePedidos, Match]
    db = pg_conn('conn_ucar')
    db.connect()
    db.create_tables(TABLES)
    db.close()
