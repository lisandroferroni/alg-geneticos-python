import numpy as np 
import random
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, asin, atan, atan2, exp
class Cromosoma:
    def __init__(self,trayectoria):
        self.trayectoria = trayectoria
        self.distancia = calculaDistanciaTotal(trayectoria)
        self.fitness=-1
    def getDistancia(self):
        return self.distancia
    def getFitness(self):
        return self.fitness
    def setFitness(self, fitness):
        self.fitness=fitness    
    def getTrayectoria(self):
        return self.trayectoria   

class ciudad:
    def __init__(self,nombre,lat,lon):
        self.nombre=nombre
        self.lat=lat
        self.lon=lon
        self.id=0    
    def setId(self,id):
        self.id=id
    def getid(self):
        return self.id
    def getLat(self):
        return self.lat
    def getLon(self):
        return self.lon
    def getNombre(self):
        return self.nombre

class LineaGrafica:
    def __init__(self,mejor,peor,promedio,trayectoria):
        self.mejor=mejor
        self.peor=peor
        self.promedio=promedio
        self.trayectoria=trayectoria
    def getMejor(self):
        return self.mejor
    def getPeor(self):
        return self.peor
    def getPromedio(self):
        return self.promedio
    def getTrayectoria(self):
        return self.trayectoria

def calculaDistanciaTotal(trayectoria):
    distanciaTotal = 0
    for x in range (0,len(trayectoria)-1):
        lat1 = ciudades[trayectoria[x]].getLat()
        lon1 = ciudades[trayectoria[x]].getLon()
        lat2 = ciudades[trayectoria[x+1]].getLat()
        lon2 = ciudades[trayectoria[x+1]].getLon()
        distanciaTotal = distanciaTotal + calc_distance(lat1, lon1, lat2, lon2)

    return distanciaTotal

def calc_distance(lat1, lon1, lat2, lon2): 
    R = 6372.8 # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
 
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    return (R * c)

def crearPoblacionInicial(num):
    poblacionInicial = []
    for _ in range (0,cantIndividuos):
        trayectoria = None
        trayectoria = []        #vacio trayectoria (sin esto quedan todas iguales)
        for i in range (0,23):  
            trayectoria.extend([i]) #crea una lista con enteros del 0 al 22
        trayectoria.pop(num)        #Elimina el num de ciudad inicial de la trayectoria   
        random.shuffle(trayectoria) #Mezcla trayectoria
        trayectoria.insert(0,num)
        trayectoria.extend([num])   #Ciudad inicial, al principio y al final de la trayectoria
        poblacionInicial.extend([Cromosoma(trayectoria)])   #Crea nuevo cromosoma con trayectoria aleatoria
    return poblacionInicial         #Devuelve lista con @cantIndividuos cromosomas 

def calcularElite(poblacion):
    poblacion = sorted(poblacion, key = lambda object : object.distancia) 
    hijos=[]
    hijos.extend([Cromosoma(poblacion[0].getTrayectoria())])
    hijos.extend([Cromosoma(poblacion[1].getTrayectoria())])
    return hijos

def crearRuleta(poblacion):
    ruleta=[]
    calcularFitness3(poblacion)          #asigna fitness con valores enteros.
    for x in range (0,len(poblacion)):  #Por cada cromosoma:
        for _ in range (0,poblacion[x].getFitness()): 
            ruleta.extend([poblacion[x].getTrayectoria()])
    return ruleta

def calcularFitness (poblacion):    #Quedan los fitnes parecidos pero no iguales
    total=0.0
    for x in range(0,len(poblacion)):
        total = total + 1/poblacion[x].getDistancia()
    for x in range(0,len(poblacion)):
        poblacion[x].setFitness(int(round(10000/poblacion[x].getDistancia()/total)))

def calcularFitness3 (poblacion):
    total = 0.0
    valor = []
    for x in range (0, len(poblacion)): 
        dist = poblacion[x].getDistancia()/10000  #dividido por mil para que quede de dos cifras como max
        valor.extend([exp(dist)])
        total = total + 1/valor[x]
    for x in range (0, len(poblacion)):
        poblacion[x].setFitness(int(round(10000/valor[x]/total)))


def calcularFitness2 (poblacion):  #muy impresiso, quedan todos fitnes iguales
    sumaDistancias = 0.0
    for dist in poblacion:
        sumaDistancias = sumaDistancias + dist.getDistancia()

    puntaje = []
    sumaPuntajes = 0.0
    for x in range(0, len(poblacion)):
        aux = 1 - (poblacion[x].getDistancia()/sumaDistancias)
        puntaje.extend([aux])
        sumaPuntajes = sumaPuntajes + aux

    for x in range(0, len(poblacion)):
        poblacion[x].setFitness(int(round(100*puntaje[x]/sumaPuntajes)))

#crossover ciclico
def ciclicCrossover(padre1,padre2):
    posActual=1 #variable aux 

    hijo1=[] #instancio los hijos
    hijo2=[]
    hijo1.append(num)
    hijo2.append(num) 
    for i in range(0, len(padre1)-2):   #les pongo a todos menos uno para indicar que no estan asignados     
        hijo1.append(-1)
        hijo2.append(-1)
    hijo1.append(num)
    hijo2.append(num)

    aux=padre1[1] #primer paso del ciclico
    
    while aux not in hijo1: #condicion de fin de ciclo
        hijo1[posActual] = aux
        aux = padre2[posActual]
        posActual = padre1.index(aux) #---> padre1[aux]       
        #posActual = padre1[padre2[posActual].getId()]#aca es donde se pone emocionante
        #aux=hijo1[posActual]
        #hijo1[posActual]=padre1[padre2.index(padre1)]

    for j in range(1, len(padre1)-1):
        if (hijo1[j] == -1):
            hijo1[j] = padre2[j]
            hijo2[j] = padre1[j]
        else:
            hijo2[j] = padre2[j]  
    #hijox1= Cromosoma(hijo1)
    #hijox2= Cromosoma(hijo2)
    return hijo1,hijo2

def mutar (padre):    
    a, b = random.randint(1,22), random.randint(1,22)
    padre[b], padre[a] = padre[a], padre[b]

    return padre

def calcularLineaGrafica (poblacion):
    poblacion = sorted(poblacion, key = lambda object : object.distancia)
    mejor=poblacion[0].getDistancia()
    trayectoria = poblacion[0].getTrayectoria()
    peor=poblacion[len(poblacion)-1].getDistancia()

    suma = 0
    for x in range (0,len(poblacion)):
        suma = suma+poblacion[x].getDistancia()
    promedio = suma/len(poblacion)

    lineaGrafica = LineaGrafica(mejor,peor,promedio,trayectoria)
    
    return lineaGrafica

def mostrarGrafica (grafica):
    lista1=[]
    lista2=[]
    lista3=[]
    for x in range (0,len(grafica)):
        lista1.extend([grafica[x].getMejor()])
        lista2.extend([grafica[x].getPeor()])
        lista3.extend([grafica[x].getPromedio()])
    plt.plot(lista1, label = "Mejor Valor")
    plt.plot(lista2, linestyle='--', label = "Peor Valor")
    plt.plot(lista3, linestyle='-.', label = "Promedio")
    plt.legend(loc="lower right")
    plt.ylim(10000.0, 30000.0)
    plt.xlabel("Generacion")
    plt.ylabel("Distancia")
    plt.show()

def cargaCiudades():
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
    for x in range (0,len(ciudades)): #No se si va a servir de algo
        ciudades[x].setId(x)
    return ciudades

def printTrayectoria(poblacion):
    poblacion = sorted(poblacion, key = lambda object : object.distancia)
    trayectoria = poblacion[0].getTrayectoria()
    print("\n\nRecorrido:\n")
    
    distanciaTotal = 0

    print (ciudades[trayectoria[0]].getNombre())
    for x in range (0,len(trayectoria)-1):
        lat1 = ciudades[trayectoria[x]].getLat()
        lon1 = ciudades[trayectoria[x]].getLon()
        lat2 = ciudades[trayectoria[x+1]].getLat()
        lon2 = ciudades[trayectoria[x+1]].getLon()
        distanciaParcial = calc_distance(lat1, lon1, lat2, lon2)
        distanciaTotal = distanciaTotal + distanciaParcial
        print (ciudades[trayectoria[x+1]].getNombre() + " - "  + str (int(distanciaParcial)) + " km.")
    print("\nDistancia total recorrida: " + str(int(poblacion[0].getDistancia())) + " km.")

def printCiudades(ciudades):
    for x in range (0, len(ciudades)):
        print(str(ciudades[x].getid()) + "- " + ciudades[x].getNombre())

def algoritmoPrincipal(poblacion):
    poblacion = sorted(poblacion, key = lambda object : object.distancia) 
    hijos=[]
    hijos.extend([poblacion[0]])
    hijos.extend([poblacion[1]])        #pasan los 2 cromosomas con menor distancia

    ruleta = crearRuleta(poblacion)         #Ruleta es lista de trayectorias
    for _ in range (0,int((len(poblacion)-len(hijos))/2)):

        padre1 = random.choice(ruleta)  #padre 1 y 2 son trayectorias seleccionadas
        padre2 = random.choice(ruleta)  #al azar de la ruleta
        
        if (random.random()<=prob_crossover):       #probabilidad de crossover
            padre1,padre2 = ciclicCrossover (padre1,padre2)
            #pass    #borrar esta linea cuando ande el crossover
        
        if (random.random()<=prob_mutacion):     #probabilidad de mutacion
            padre1 = mutar(padre1)              
            padre2 = mutar(padre2)
        
        hijos.extend([Cromosoma(padre1),Cromosoma(padre2)])

    return hijos


#variables
ciclos=1000
cantIndividuos=30
prob_crossover=0.9
prob_mutacion=0.1

#Main

ciudades = cargaCiudades()
print ("Ingrese num ciudad inicial (0-22)")
printCiudades(ciudades)
num = int(input())
#num = 0
grafica=[]

poblacion = crearPoblacionInicial(num)
grafica.extend([calcularLineaGrafica(poblacion)])

for _ in range (0,ciclos):
    poblacion = algoritmoPrincipal(poblacion)
    grafica.extend([calcularLineaGrafica(poblacion)])
printTrayectoria(poblacion)
mostrarGrafica(grafica)

print()
