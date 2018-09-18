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

elemento.extend([Elemento(1800,72)])
elemento.extend([Elemento(600,36)])
elemento.extend([Elemento(1200,60)])

volMax=3000
n=len(elemento)
utilidadTotal=0
valorTotal=0
volAcu=0

i=0

mochila=[]

#elemento.sort(cpm=elemento.cmpUtilidad)

elemento.sort(key=lambda x: x.utilidad, reverse=True)



while (volAcu<volMax) and (i<(n-1)):
    if ((volAcu+(elemento[i].volumen))<=volMax):
        mochila.extend([elemento[i]])
        volAcu=volAcu+elemento[i].volumen
        utilidadTotal=utilidadTotal+elemento[i].utilidad
        valorTotal=valorTotal+elemento[i].valor
        i+=1
    else:
        i+=1    



for x in range (0, len(mochila)):
    print(mochila[x].volumen)
print(utilidadTotal)
print(valorTotal)