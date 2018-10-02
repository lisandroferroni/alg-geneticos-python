import numpy as np 
import random
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, asin, atan, atan2


class ciudad:
    def __init__(self,nombre,lat,lon):
        self.nombre=nombre
        self.lat=lat
        self.lon=lon
        self.estado=0
    
    def setEstado(self,estado):
        self.estado=estado

    def getEstado(self):
        return self.estado
    def getLat(self):
        return self.lat
    def getLon(self):
        return self.lon
    def getNombre(self):
        return self.nombre


def calc_distance(lat1, lon1, lat2, lon2): 
  R = 6372.8 # Earth radius in kilometers
 
  dLat = radians(lat2 - lat1)
  dLon = radians(lon2 - lon1)
  lat1 = radians(lat1)
  lat2 = radians(lat2)
 
  a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
  c = 2*asin(sqrt(a))
 
  return (R * c)
def printCiudades (ciudades):
    for x in range (0, len(ciudades)):
        print(str(x) + "- " + ciudades[x].getNombre())


ciudades=[]
ciudades.extend([ciudad("Buenos Aires",-34.599722, -58.381944)])
ciudades.extend([ciudad("Córdoba",-31.416667, -64.183333)])
ciudades.extend([ciudad("S. F. del valle de Catamarca",-28.468611, -65.779167)])
ciudades.extend([ciudad("Resistencia",-27.451389, -58.986667)])
ciudades.extend([ciudad("Rawson",-43.3, -65.1)])
ciudades.extend([ciudad("Corrientes",-27.483333, -58.816667)])
ciudades.extend([ciudad("Paraná",-31.744444, -60.5175)])
ciudades.extend([ciudad("Formosa",-26.184722, -58.175833)])
ciudades.extend([ciudad("San S. de Jujuy",-24.185556, -65.299444)])
ciudades.extend([ciudad("Santa Rosa",-36.620278, -64.290556)])
ciudades.extend([ciudad("La Rioja",-29.413056, -66.855833)])
ciudades.extend([ciudad("Mendoza",-32.883333, -68.833333)])
ciudades.extend([ciudad("Posadas",-27.366667, -55.896944)])
ciudades.extend([ciudad("Neuquén",-38.95735, -68.045533)])
ciudades.extend([ciudad("Viedma",-40.8, -63)])
ciudades.extend([ciudad("Salta",-24.788333, -65.410556)])
ciudades.extend([ciudad("San Juan",-31.5375, -68.536389)])
ciudades.extend([ciudad("San Luis",-33.277222, -66.3525)])
ciudades.extend([ciudad("Rio Gallegos",-51.633333, -69.233333)])
ciudades.extend([ciudad("Santa Fe",-31.633333, -60.7)])
ciudades.extend([ciudad("Santiago del Estero",-27.784444, -64.266944)])
ciudades.extend([ciudad("Ushuaia",-54.807222, -68.304444)])
ciudades.extend([ciudad("S. M. de Tucumán",-26.816667, -65.216667)])

print ("Ingrese num ciudad inicial (0-22)")
printCiudades(ciudades)
num = int(input())
ciudadActual = ciudades[num]          #El num que ingresa es ciudad inicial y final del recorrido
ciudadFinal = ciudades[num]
distanciaTotal = 0                    #Inicializa el acumulador de distancias
ciudadActual.setEstado(1)             #Marca ciudad inicial como usada

print("Recorrido:\n\n" + ciudadActual.getNombre())
for x in range (0,22):
    distanciaMin = 5000.0             #Se asigna numero elevado para calcular el menor luego
    ciudadProxima = None              #Libera la variable

    for y in range (0,23):        
        if (ciudades[y].getEstado()==1): #Si la ciudad ya fue usada, no se compara distancia
            continue
        
        distanciaActual = calc_distance(ciudadActual.getLat(),ciudadActual.getLon(),ciudades[y].getLat(),ciudades[y].getLon())
        if (distanciaActual < distanciaMin):    #Busca ciudad mas cercana y guarda distancia y ciudad
            distanciaMin = distanciaActual
            ciudadProxima = ciudades[y]    
    
    distanciaTotal = distanciaTotal + distanciaMin   #Acumula distancia total
    ciudadActual = ciudadProxima                     #Actualiza ciudad actual con la de menor distancia,   
    ciudadActual.setEstado(1)                        #y la marca como usada
    print (ciudadActual.nombre + "- " + str (int(distanciaMin)) + " km.")

distanciaAInicial = calc_distance(ciudadActual.getLat(),ciudadActual.getLon(),ciudadFinal.getLat(),ciudadFinal.getLon())
distanciaTotal = distanciaTotal + distanciaAInicial
print (ciudadFinal.nombre + "- " + str (int(distanciaAInicial)) + " km.")
print("\nLa distancia total recorrida es: " + str(int(distanciaTotal)) + " km.")