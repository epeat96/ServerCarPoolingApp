from peewee import Model
from orm.conn.db import pg_conn

class BaseModel(Model):
    class Meta:
        database = pg_conn('conn_ucar')