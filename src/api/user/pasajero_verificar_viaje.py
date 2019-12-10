#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from json import loads
import subprocess as sub
from flask import request
from peewee import Select
from flask import Blueprint
from flask import jsonify
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.itinerario import Itinerario
from orm.model.ucar.match import Match 
import time
import math

INDEX = 'verificar'
PATH = '/ucar/pasajero/viaje/'
index_pasajero_verificar_viaje = Blueprint(INDEX, __name__)

@index_pasajero_verificar_viaje.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def BuscarChofer():
	#Posicion del Pasajero 
	posicion=(-57.647976859562334,-25.285515826523806) #TODO conseguir de la base de datos
	#Lista de Choferes Online
	coordenadas=[("-57.647976859562334,-25.285515826523806","-57.63543469077945,-25.324514646565376")] #TODO conseguir de la base de datos
	rutas = genRtLst(coordenadas)
	Min = minRoute(posicion,rutas)
	i=0
	for ruta in rutas:
		if ruta == Min:
			inicioV=coordenadas[i][0].split(",")
			finV=coordenadas[i][1].split(",")
			respuesta ={ "respuesta":"TRUE","longitudInicio":inicioV[1],"latitudInicio":inicioV[0],"longitudFin":finV[1],"latitudFin":finV[0]} 
			query = Itinerario.select().where(
							(Itinerario.latitudOrig == respuesta["latitudInicio"]) &
							(Itinerario.longitudOrig == respuesta["longitudInicio"]) &
							(Itinerario.latitudDst == respuesta["latitudFin"]) &
							(Itinerario.longitudDst == respuesta["longitudFin"]) 
							)
			if query.exists():
				for result in query:
					idChofer = result.fk_persona_id
					respuesta["idChofer"] = str(idChofer)
					#match = { "fk_chofer_id" : idChofer , "latitud" : "-57.647976859562334" , "longitud" : "-25.285515826523806"  , "estado" : "atentido" }
					new = Match()
					new.fk_chofer_id = result.fk_persona_id
					new.latitud = "-57.647976859562334"
					new.longitud = "-25.285515826523806"
					new.estado = "atentido"
					new.save()
					return respuesta
			else:
				return "Algo salio mal"
		i=i+1
def genRtLst(coordenadas):
    rutas=[]
    for par in coordenadas:
        rutas.append(getPuntos(par[0],par[1]))
    return rutas
#Retorna los puntos que conforman una ruta a travez del punto inicial y el punto final
def getPuntos(inicio,fin):
    diccionario=loads(str(sub.check_output(["/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/curl.sh",inicio,fin]),encoding="UTF-8"))
    i = 0
    puntos = []
    for step in diccionario["matchings"][0]["legs"][0]["steps"]:
        puntos.append((step["maneuver"]["location"][0],step["maneuver"]["location"][1]))
        for intersection in step["intersections"]:
            puntos.append((intersection["location"][0],intersection["location"][1]))
    return puntos
#Retorna el punto mas cercano a la posicion dada (un punto a una ruta)
def rtCmp(posicion,puntos):
    distancias=[]
    for punto in puntos:
       distancias.append(dist(posicion,punto)) 
    Min =  min(distancias)
    i = 0
    for distancia in distancias:
        if distancia == Min:
            return puntos[i]
        i = i + 1
#Distancia de un punto a, a un punto b
def dist( a , b ):
    distance = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return distance
#Retorna la ruta mas cercana
def minRoute(posicion,rutas):
    puntos = []
    for ruta in rutas:
        puntos.append(rtCmp(posicion,ruta))
    distancias=[]
    for punto in puntos:
       distancias.append(dist(posicion,punto)) 
    Min =  min(distancias)
    i = 0
    for distancia in distancias:
        if distancia == Min:
            return rutas[i]
        i = i + 1
