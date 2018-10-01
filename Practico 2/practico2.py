import numpy as np 
import random
import matplotlib.pyplot as plt

class Cromosoma:
    def __init__(self,binario):
        self.binario=binario
        self.decimal=binarioADecimal(binario)
        self.valor=f(binarioADecimal(binario))
        self.fitness=-1
    def getValor(self):
        return self.valor
    def getBinario(self):
        return self.binario
    def getFitness(self):
        return self.fitness
    def getDecimal(self):
        return self.decimal
    def setFitness(self, fitness):
        self.fitness=fitness
   
    

class Grafica:
    def __init__(self,mejor,peor,promedio,mejor_bin):
        self.mejor=mejor
        self.peor=peor
        self.promedio=promedio
        self.mejor_bin=mejor_bin
    def getMejor(self):
        return self.mejor
    def getPeor(self):
        return self.peor
    def getPromedio(self):
        return self.promedio
    def getMejor_bin(self):
        return self.mejor_bin


# Pasando un binario devuelve el valor en decimal (float)
def binarioADecimal (binario):
    num=0
    for y in range (0,len(binario)):
        num=num+binario[y]*2**(len(binario)-1-y)
    return num

# Funcion del enunciado
def f (decimal):
    return ((decimal/coeficiente)**2)

# Devuelve cantidad de objetos con binario(30 bits), decimal y el valor evaluando la f
def crearPoblacionInicial (cantIndividuos):
    poblacion=[]
    for _ in range (0,cantIndividuos):
        binario=np.random.randint(2, size=30)
        poblacion.extend([Cromosoma(binario)])
    return poblacion 

# Setea el valor de fitness a cada cromosoma. 
# fitness= valor de la funcion aplicada al cromosoma sobre el total
# de los valores de la poblacion 
def calcularFitness (poblacion):
    total=0.0
    for x in range(0,len(poblacion)):
        total = total + poblacion[x].getValor()
    for x in range(0,len(poblacion)):
        poblacion[x].setFitness(int(round(100*poblacion[x].getValor()/total)))

# Toma 2 cromosomas random de la ruleta, los cruza con prob_crossover de probabilidad
# a partir de un punto de corte aleatorio.
# Muta cromosoma con prob_mutacion de probabilidad
# Devuelve 10 cromosomas hijos
def crossover (poblacion):
    
    #Elite
    poblacion = sorted(poblacion, key = lambda object : object.valor, reverse=True) 
    hijos=[]
    hijos.extend([poblacion[0]])
    hijos.extend([poblacion[1]])
    #Fin Elite

    ruleta=crearRuleta(poblacion)
    
    for _ in range (0,int((len(poblacion)-len(hijos))/2)):
        
        cromosoma1_bin=ruleta[np.random.randint(0, len(ruleta))]
        cromosoma2_bin=ruleta[np.random.randint(0, len(ruleta))]
                
        if (random.random()<=prob_crossover): 
            puntoCorte=(np.random.randint(1, len(cromosoma1_bin)))
            aux=np.random.randint(2, size=30)
            for x in range (0,len(cromosoma2_bin)):
                aux[x]=cromosoma2_bin[x]

            for x in range (puntoCorte,len(cromosoma2_bin)):
                cromosoma2_bin[x]=cromosoma1_bin[x]
                cromosoma1_bin[x]=aux[x]
        
        if (random.random()<=prob_mutacion):
            cromosoma1_bin=mutar(cromosoma1_bin)
            cromosoma2_bin=mutar(cromosoma2_bin)
       
        hijos.extend([Cromosoma(cromosoma1_bin), Cromosoma(cromosoma2_bin)])
    return hijos    
    
# Cambia un bit aleatorio del cromosoma 
def mutar (cromosoma_bin):
    aux=np.random.randint(2, size=30)
    for x in range (len(cromosoma_bin)):
        aux[x]=cromosoma_bin[x]
    
    gen=random.randint(0,len(aux)-1)
    aux[gen]=abs(cromosoma_bin[gen]-1)
    return aux

# Devuelve un array de 100* binarios 
# (los 10 cromosomas repetidos segun su fitness
# redondeado, puede ser que la ruleta tenga menos de 100)
def crearRuleta(poblacion):
    ruleta=[]
    calcularFitness(poblacion)
    for x in range (0,len(poblacion)):
        for _ in range (0,poblacion[x].getFitness()):
            ruleta.extend([poblacion[x].getBinario()])
    return ruleta

def calcularLineaGrafica (poblacion):
    mejor=poblacion[0].getValor()
    mejor_bin=poblacion[0].getBinario()
    for x in range (1,len(poblacion)):
        if (poblacion[x].getValor()>mejor):
            mejor=poblacion[x].getValor()
            mejor_bin=poblacion[x].getBinario()

    peor=poblacion[0].getValor()
    for x in range (1,len(poblacion)):
        if (poblacion[x].getValor()<peor):
            peor=poblacion[x].getValor()
    suma=0
    for x in range (0,len(poblacion)):
        suma=suma+poblacion[x].getValor()
    promedio=suma/len(poblacion)
    lineaGrafica=Grafica(mejor,peor,promedio,mejor_bin)
    
    return lineaGrafica
    
# Imprime una grafica con el mejor valor, peor valor, y promedio de todos los 
# valores para cada generacion
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
    plt.ylim(0, 1.0)
    plt.xlabel("Generacion")
    plt.ylabel("Valor")
    plt.show()

#variables
ciclos=300
coeficiente=(2**30)-1
cantIndividuos=10
prob_crossover=0.75
prob_mutacion=0.5

#"main"
poblacion = crearPoblacionInicial(cantIndividuos)
grafica=[]
grafica.extend([calcularLineaGrafica(poblacion)])

for x in range (0,ciclos):
    poblacion=crossover(poblacion)   
    grafica.extend([calcularLineaGrafica(poblacion)])
    
mostrarGrafica(grafica)
