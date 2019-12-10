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

class Viaje(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	fecha = DateField(null=False, formats='%d-%m-%Y', default=datetime.now().strftime("%d-%m-%Y"))
	hora = TimeField(null=False, formats='%H:%M:%S', default=datetime.now().strftime("%H:%M:%S"))
	fk_chofer = ForeignKeyField(null=False,model=Persona,field=Persona.id)	#Chofer
	fk_pasajero = ForeignKeyField(null=False,model=Persona,field=Persona.id) #Pasajero
	latitud = FloatField(null=False)	
	longitud = FloatField(null=False)
	estado = CharField(null=False, default='completo')