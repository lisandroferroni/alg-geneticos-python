import numpy as np 
import random

class Cromosoma:
    def __init__(self,binario):
        self.binario=binario
        self.decimal=binarioADecimal(binario)
        self.valor=f(binarioADecimal(binario))
        self.fitness=-1.0
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



#Pasando un binario devuelve el valor en decimal (float)
def binarioADecimal (binario):
    num=0
    for y in range (0,len(binario)):
        num=num+binario[y]*2**(len(binario)-1-y)
    return num

#devuelve cantidad de objetos con binario(30 bits), decimal y el valor evaluando la f
def crearPoblacionInicial (cantIndividuos):
    cromosomas=[]
    for _ in range (0,cantIndividuos):
        binario=np.random.randint(2, size=30)
        cromosomas.extend([Cromosoma(binario)])
    return cromosomas 

def calcularFitness (cromosomas):
    total=0.0
    for x in range(0,len(cromosomas)):
        total = total + cromosomas[x].getValor()
    for x in range(0,len(cromosomas)):
        cromosomas[x].setFitness(int(round(100*cromosomas[x].getValor()/total)))

#funcion del enunciado
def f (dec):
    return ((dec/coef)**2)

#Toma 2 cromosomas random de la ruleta, los cruza con prob_crossover de probabilidad
#a partir de un punto de corte aleatorio.
#Muta bit por bit con prob_mutacion de probabilidad
#Devuelve 10 cromosomas hijos
def crossover (cromosomas):
    ruleta=crearRuleta(cromosomas)
    hijos=[]
    for _ in range (0,int(len(cromosomas)/2)):
        random.random()
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
        cromosoma1_bin=mutar(cromosoma1_bin)
        cromosoma2_bin=mutar(cromosoma2_bin)
       

        hijos.extend([Cromosoma(cromosoma1_bin)])
        hijos.extend([Cromosoma(cromosoma2_bin)])
        
    return hijos
    

#Cambia un bit del cromosoma con prob_mutacion de prob 
def mutar (cromosoma_bin):
    for x in range (0,len(cromosoma_bin)):
        aux=random.random()
        if (random.random()<=prob_mutacion):
            cromosoma_bin[x]=abs(cromosoma_bin[x]-1)
    return cromosoma_bin

#Devuelve un array (ruleta) de 100 binarios 
# (los 10 cromosomas repetidos segun su fitness)
def crearRuleta(cromosomas):
    ruleta=[]
    for x in range (0,cantIndividuos):
        for _ in range (0,cromosomas[x].getFitness()):
            ruleta.extend([cromosomas[x].getBinario()])
    return ruleta

def calcularGrafica (poblacion):
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

#Solo son prints de las cosas de los objetos
def mostrarDecimales(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].decimal)
def mostrarBinarios(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].binario)
def mostrarValores(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].getValor())
def mostrarRuleta(ruleta):
    for x in range (0,100):
        print (ruleta[x])
    print("\n")


#variables

ciclos=20
coef=(2**30)-1
cantIndividuos=20
prob_crossover=0.75
prob_mutacion=0.01

#"main"
cromosomas = crearPoblacionInicial(cantIndividuos)

grafica=[]
grafica.extend([calcularGrafica(cromosomas)])

text_file = open("Salida.txt", "w")
text_file.write("Mejor\t\t\tPeor\t\t\tPromedio\n")
print(grafica[0].getMejor_bin(),"\t",grafica[0].getMejor(), "\t", grafica[0].getPeor(), "\t", grafica[0].getPromedio())
text_file.write(str(grafica[0].getMejor_bin()) + "\t"+str(grafica[0].getMejor())+"\t"+str(grafica[0].getPeor())+"\t"+str(grafica[0].getPromedio())+"\n")

for x in range (0,ciclos):
    calcularFitness(cromosomas)
    cromosomas=crossover(cromosomas)
    
    grafica.extend([calcularGrafica(cromosomas)])
    #print(grafica[x+1].getMejor_bin(),"\t", grafica[x+1].getMejor(), "\t", grafica[x+1].getPeor(), "\t", grafica[x+1].getPromedio())
    text_file.write(str(grafica[x+1].getMejor_bin()) + "\t"+str(grafica[x+1].getMejor())+"\t"+str(grafica[x+1].getPeor())+"\t"+str(grafica[x+1].getPromedio())+"\n")
