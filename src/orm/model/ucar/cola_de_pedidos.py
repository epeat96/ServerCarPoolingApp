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

class ColaDePedidos(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	latitudOrig = CharField(null=False)	
	longitudOrig = CharField(null=False)
	latitudDst = CharField(null=False)	
	longitudDst = CharField(null=False)
	fecha = DateField(null=True,formats='%d-%m-%Y')
	hora = TimeField(null=True,formats='%H:%M')
	estado = CharField(null=True,max_length=255)
	fk_persona = ForeignKeyField(null=False,model=Persona,field=Persona.id)
	fk_chofer = ForeignKeyField(null=True,model=Persona,field=Persona.id)
