import numpy as np 
class Prueba:
    def __init__(self,num):
        self.num=num


class Cromosoma:
    def __init__(self,binario):
        self.binario=binario
        self.decimal=binarioADecimal(binario)
        self.valor=f(binarioADecimal(binario))
        self.fitness=-1.0

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
    total=0
    for x in range(0,len(cromosomas)):
        total = total + cromosomas[x].valor
    for x in range(0,len(cromosomas)):
        cromosomas[x].fitness=int(round(100*cromosomas[x].valor/total))  

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
        cromosoma1_bin=ruleta[np.random.randint(1, 100)]
        cromosoma2_bin=ruleta[np.random.randint(1, 100)]
        
        if (np.random.randint(1, 100)<=prob_crossover):
            puntoCorte=(np.random.randint(1, 30))
            aux=cromosoma2_bin
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
        if (np.random.randint(1, 100)<=prob_mutacion):
            cromosoma_bin[x]=abs(cromosoma_bin[x]-1)
    return cromosoma_bin

#Devuelve un array (ruleta) de 100 binarios 
# (los 10 cromosomas repetidos segun su fitness)
def crearRuleta(cromosomas):
    ruleta=[]
    for x in range (0,10):
        for _ in range (0,cromosomas[x].fitness):
            ruleta.extend([cromosomas[x].binario])
    return ruleta

#Solo son prints de las cosas de los objetos
def mostrarDecimales(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].decimal)
def mostrarBinarios(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].binario)
def mostrarValores(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].fitness)
def mostrarRuleta(ruleta):
    for x in range (0,100):
        print (ruleta[x].fitness)
def mostrarHijos(hijos):
    for x in range (0,10):
        print (hijos[x].binario)
        print (hijos[x].decimal)


#var
prob_crossover=75
prob_mutacion=5
ciclos=20
coef=2**30-1
cantIndividuos=10

cromosomas = crearPoblacionInicial(cantIndividuos)

#mostrarBinarios(cromosomas)
#mostrarDecimales(cromosomas)
#calcularFitness((cromosomas))
#mostrarValores(cromosomas)
#mostrarHijos(crossover(cromosomas))


def asd (objeto):
    objeto.num=0

pruebaa=Prueba(4)
print (pruebaa.num)
asd(pruebaa)
print(pruebaa.num)

