#PROGRA DE ABEJAS Y  FLORES
# Imports
import pygame
from random import randint
from flor import Flor
from abejas import Abeja
from numpy import binary_repr

pygame.init()


#POBLACION INICIAL
poblacionAbejas = []
poblacionFlores = []


#CONVERSOR
#E: Un numero
#S: Un numero binario
#D: Convierte el numero dado en binario
def decimalToBinary(n):  
    return bin(n).replace("0b", "")


#PRIMERA GEN DE FLORES

def genFlowerPoblation(maxPop):

    flowersPos = []

    for i in range(0, maxPop):


        dna = []
        n = randint(0, 7)
        
        i = randint(0, 127)
        j = randint(0, 127)
        pos = (i, j)
        
        while pos in flowersPos:

            i = randint(0, 127)
            j = randint(0, 127)
            pos = (i, j)

        flowersPos.append(pos)
        
        genI = decimalToBinary(i)
        genJ = decimalToBinary(j)
        genColor = decimalToBinary(n)
        
        if len(genI) < 7:

            for i in range(0, 7-len(genI)):

                dna.append(0)
                
        for bit in genI:

            dna.append(int(bit))

        if len(genJ) < 7:

            for i in range(0, 7-len(genJ)):

                dna.append(0)
                
        for bit in genJ:

            dna.append(int(bit))

        if len(genColor) < 3:
            
            for i in range(0, 3-len(genColor)):

                dna.append(0)
                
        for bit in genColor:

            dna.append(int(bit))

        newFlower = Flor(dna)
        poblacionFlores.append(newFlower)


    #for flor in poblacionFlores:

     #   print(flor.dna)

"""
Para crear una nueva generacion a partir de la anterior
se recorre la lista de objetos, para cada uno se llama a la función que genera
un nuevo individuo a partir de los genes recolectadosy lo retorna para agregarlo
a una nueva lista de objetos

El problema princípal con las flores es evitar que queden en la misma posicion

Cruce, mutacion, nueva generación
"""
          
#PRIMERA GEN DE ABEJAS--------------------------------------

def genAbejasGenerator(n):
    
    global poblacionAbejas

    for i in range(0,n):

        newBeeDNA = []

        #COLOR
        newColor = randint(0, 7)
        #DIRECCION
        newDir = randint(0, 7)
        #DISTANCIA
        newDist = randint(0, 63)
        #TIPO
        newTipo = randint(0, 3)
        #ANGULO DESVIACION (PROVISIONAL)
        newAngulo = randint(0,31)
        #DNA ABEJA
        newBeeDNA = transBinaryFormat(newColor,3) + transBinaryFormat(newDir,3) + transBinaryFormat(newAngulo,6) + transBinaryFormat(newDist,6) + transBinaryFormat(newTipo,2)
        #NUEVA ABEJA
        newBee = Abeja(newBeeDNA)
        poblacionAbejas.append(newBee)
    """  
    for j in range(0,len(poblacionAbejas)):
        print()
        print("Abeja #",j)
        poblacionAbejas[j].decodeInfo()
        poblacionAbejas[j].printInfo()
        print()

    return
    """

    
        
def transBinaryFormat(data,rangeBits):
    
    bitChain = decimalToBinary(data)
    dnaChain = []

    if len(bitChain) < rangeBits:
        for i in range(0, rangeBits-len(bitChain)):
            dnaChain.append(0)
                
    for bit in bitChain:
            
        dnaChain.append(int(bit))
    
    return dnaChain
                

#GUI
"""
# IMAGENES
# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
# Crea la ventana
garden = pygame.display.set_mode((1300,800))

# Nombre de la ventana
pygame.display.set_caption('Bees&Flowers by Sven&Rev')
reloj = pygame.time.Clock()

# FUENTE
font = pygame.font.SysFont("Minecraft", 20)
font2 = pygame.font.SysFont("Minecraft", 40)
font3 = pygame.font.SysFont("Minecraft", 10)
"""
