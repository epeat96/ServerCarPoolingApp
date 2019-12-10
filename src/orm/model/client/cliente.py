#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import Model
from peewee import AutoField
from peewee import CharField
from orm.conn.base import BaseModel

class Cliente(BaseModel):
    id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
    email = CharField(null=False, unique=True, max_length=255) # VARCHAR(255), UNIQUE, NOT NULL
