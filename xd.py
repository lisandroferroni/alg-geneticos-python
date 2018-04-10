import numpy as np 
class Cromosoma:
    def __init__(self,binario,decimal,valor):
        self.binario=binario
        self.decimal=decimal
        self.valor=valor
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
        decimal=binarioADecimal(binario)
        valor=f(decimal)
        cromosomas.extend([Cromosoma(binario,decimal,valor)])
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

"""
def crossover (cromosomas):
    ruleta=crearRuleta(cromosomas)
    for x in range (0,len(cromosomas)/2):
        cromosoma1=ruleta[np.random.randint(1, 100)]
        cromosoma2=ruleta[np.random.randint(1, 100)]
        
        if (np.random.randint(1, 100)<=prob_crossover):
            puntoCorte=(np.random.randint(1, 30))
            
            """



def crearRuleta(cromosomas):
    ruleta=[]
    for x in range (0,10):
        for _ in range (0,cromosomas[x].fitness):
            ruleta.extend([cromosomas[x]])
    return ruleta

        



#def mutacion():

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

#var
prob_crossover=75
prob_mutacion=5
ciclos=20
coef=2**30-1
cantIndividuos=10

cromosomas = crearPoblacionInicial(cantIndividuos)

mostrarBinarios(cromosomas)
mostrarDecimales(cromosomas)
calcularFitness((cromosomas))
mostrarValores(cromosomas)