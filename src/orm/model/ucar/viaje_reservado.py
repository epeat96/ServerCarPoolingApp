#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import Model
from peewee import AutoField
from peewee import CharField
from peewee import FloatField
from peewee import BooleanField
from peewee import DateField
from peewee import TimeField
from peewee import ForeignKeyField  
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class ViajeReservado(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	latitudOrig = FloatField(null=False)	
	longitudOrig = FloatField(null=False)
	latitudDst = FloatField(null=False)	
	longitudDst = FloatField(null=False)
	fecha = DateField(null=False,formats='%d-%m-%Y')
	hora = TimeField(null=False,formats='%H:%M')
	fk_persona = ForeignKeyField(null=False,model=Persona,field=Persona.id)
