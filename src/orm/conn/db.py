#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from os import path
from json import load
from peewee import PostgresqlDatabase

# función		:   pg_conn()
# parametros	:	archivo de conexión
# utilidad		: 	lee el archivo de configuracíon de la bd la
#                   cual contiene los parametros de conexión,
#                   utiliza los mismos para definir la conexión.
# retorno		:   instancia de conexión a la base de datos
# detalles		: 	ninguno
def pg_conn(jsonfile):
    # obtiene la dirección del directorio del script actual
    current_file_dir = path.dirname(__file__)
    # concatenación del nombre del archivo cfg
    # y su ubicación (directorio actual)
    cfg = path.join(current_file_dir, jsonfile + '.json')
    # manejo de archivos
    with open(cfg) as f:
        # se lee todo el contenido
        # del archivo json, se almacena
        # en data en forma de diccionario {clave:valor}
        data = dict(load(f))
    # retorno de instancia de conexión
    return PostgresqlDatabase(**data)
