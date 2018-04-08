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
        cromosomas[x].fitness=cromosomas[x].valor/total       

#funcion del enunciado
def f (dec):
    return ((dec/coef)**2)

#Solo son prints de las cosas de los objetos
def mostrarDecimales(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].decimal)
def mostrarBinarios(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].binario)
def mostrarValores(cromosomas):
    for x in range (0,len(cromosomas)):
        print (cromosomas[x].valor)

#var
prob_crossover=0.75
prob_mutacion=0.05
ciclos=20
coef=2**30-1
cantIndividuos=10

cromosomas = crearPoblacionInicial(cantIndividuos)

mostrarBinarios(cromosomas)
mostrarDecimales(cromosomas)
mostrarValores(cromosomas)
calcularFitness((cromosomas))
print ("as")


