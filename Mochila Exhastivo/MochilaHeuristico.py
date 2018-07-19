import numpy as np 
class Elemento:
    def __init__(self,volumen,valor):
        self.volumen=volumen
        self.valor=valor
   
def utilidad(e):
    return (e.volumen/e.valor)


def valor (s):
    suma=0
    for x in range (0, len (s)):
        if s[x]==1:
            suma=suma+elemento[x].valor
    return suma


def calcUtilidades(elementos):
    utilidades=[]
    for i in range (0,n):
        utilidades.extend(utilidad(elementos[i]))
    return utilidades 
elemento=[]
elemento.extend([Elemento(150,20)])
elemento.extend([Elemento(325,40)])
elemento.extend([Elemento(600,50)])
elemento.extend([Elemento(805,36)])
elemento.extend([Elemento(430,25)])
elemento.extend([Elemento(1200,64)])
elemento.extend([Elemento(770,54)])
elemento.extend([Elemento(60,18)])
elemento.extend([Elemento(930,46)])
elemento.extend([Elemento(353,28)])
volMax=4200
n=10

utilidades=calcUtilidades(elemento)