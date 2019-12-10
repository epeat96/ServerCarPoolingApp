#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import AutoField
from peewee import CharField
from peewee import IntegerField
from peewee import DateTimeField
from peewee import DateTimeField
from peewee import DateField
from peewee import FloatField
from peewee import TimeField
from peewee import ForeignKeyField
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class Itinerario(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	latitudOrig = CharField(null=False, max_length=255)	
	longitudOrig = CharField(null=False, max_length=255)
	latitudDst = CharField(null=False, max_length=255)	
	longitudDst = CharField(null=False, max_length=255)
	dia = CharField(null=False, max_length=255)
	horaEntrada = TimeField(null=False,formats='%H:%M')
	horaSalida = TimeField(null=False,formats='%H:%M')
	fk_persona = ForeignKeyField(null=False,model=Persona,field=Persona.id)
