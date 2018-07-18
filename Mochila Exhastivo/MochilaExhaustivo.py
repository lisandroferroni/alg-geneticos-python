import numpy as np 
import random

class Elemento:
    def __init__(self,volumen,valor):
        self.volumen=volumen
        self.valor=valor

def valor (s):
    suma=0
    for x in range (0, len (s)):
        if s[x]==1:
            suma=suma+elemento[x].valor
    return suma

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

#Problema de maximizacion, pag 19 pdf
nivel=0
s= [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
voa = -1
soa = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
suma = 0
while (nivel!=-1):
    
    #Generar
    
    s[nivel] = s[nivel] + 1
    if s[nivel]==1:
        suma=suma+elemento[nivel].volumen
        #Solucion                      ]
    if (nivel==len(s)-1) and (suma<volMax) and (valor(s)>voa):
        voa=valor(s)
        print (voa)
        for x in range (0,len(s)):
            soa[x]=s[x]
        #Criterio
    if (nivel<len(s)-1) and (suma<=volMax):
        nivel = nivel + 1
    else:                   #NOT MasHermanos
        while (nivel>-1) and (s[nivel]>=1):
            #Retroceder
            suma=suma-elemento[nivel].volumen*s[nivel]
            s[nivel]=-1
            nivel=nivel-1

