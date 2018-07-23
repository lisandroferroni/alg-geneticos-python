import numpy as np 
class Elemento:
    def __init__(self,volumen,valor):
        self.volumen=volumen
        self.valor=valor
        self.utilidad=volumen/valor

        def cmpUtilidad(self,elemento):

            if self.utilidad < elemento.utilidad:

                rst = -1

            elif self.utilidad > elemento.utilidad:

                rst = 1

            else:

                rst = 0

            return rst
   
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
n=len(elemento)

utilidadTotal=0
valorTotal=0
volAcu=0
i=0
mochila=[]
#elemento.sort(cpm=elemento.cmpUtilidad)
elemento.sort(key=lambda x: x.utilidad, reverse=True)

while (volAcu<volMax) and (i<(n-1)):
    if ((volAcu+(elemento[i].volumen))<volMax):
        mochila.extend([elemento[i]])
        volAcu=volAcu+elemento[i].volumen
        i+=1
        utilidadTotal=utilidadTotal+elemento[i].utilidad
        valorTotal=valorTotal+elemento[i].valor
    else:
        i+=1    

print(utilidadTotal)
print(valorTotal)
