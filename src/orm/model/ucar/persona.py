#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import Model
from peewee import AutoField
from peewee import CharField
from peewee import BooleanField
from peewee import DateTimeField
from datetime import datetime
from orm.conn.base import BaseModel

class Persona(BaseModel):
    id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
    nombre = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    apellido = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    email = CharField(null=False, unique=True, max_length=255) # VARCHAR(255), UNIQUE, NOT NULL
    institucion = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    password = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    conexion = DateTimeField(null=True, formats='%d-%m-%Y %H:%M:%S', default=datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    conductor = BooleanField(null=True, default=False)