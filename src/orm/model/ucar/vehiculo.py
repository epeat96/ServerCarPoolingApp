#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import AutoField
from peewee import CharField
from peewee import IntegerField
from peewee import ForeignKeyField
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class Vehiculo(BaseModel):
    id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
    fkPersona = ForeignKeyField(null=False, unique=True, model=Persona, field=Persona.id) # FK, one-to-one, Persona->Vehiculo
    marca = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    modelo = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    color = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    chapa = CharField(null=False, unique=True, max_length=255) # VARCHAR(255), NOT NULL, UNIQUE
    asiento = IntegerField(null=False) # INTEGER, NOT NULL