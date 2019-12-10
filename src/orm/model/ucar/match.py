#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import AutoField
from peewee import CharField
from peewee import DateField
from peewee import FloatField
from peewee import TimeField
from peewee import ForeignKeyField
from datetime import datetime
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class Match(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	fk_chofer = ForeignKeyField(null=False,model=Persona,field=Persona.id)	#Chofer
	latitud = CharField(null=False)	
	longitud = CharField(null=False)
	estado = CharField(null=False, default='no atendido')
