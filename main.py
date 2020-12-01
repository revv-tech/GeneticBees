#PROGRA DE ABEJAS Y  FLORES
# Imports
import pygame
from random import randint
from flor import Flor
from abejas import Abejas
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
          
#PRIMERA GEN DE ABEJAS
def genAbejasGenerator(n):
    global poblacionAbejas
    for i in range(n):

        newBee = []

        #COLOR
        newColor = randint(0, 8)
        #DIRECCION
        newDir = randint(0, 8)
        #DISTANCIA
        newDist = randint(0, 64)
        #TIPO
        newTipo = randint(0, 3)
        #ANGULO DESVIACION (PROVISIONAL)
        newAngulo = randint(0,31)

        newBee = [newColor] + [newDir] + [newDist] + [newTipo] + [newAngulo]
        newBeeAux = [binary_repr(newColor)]+[binary_repr(newDir)]+ [binary_repr(newDist)] + [binary_repr(newTipo)] + [binary_repr(newAngulo)]
        print(i)
        print(newBee)
        print(newBeeAux)
        poblacionAbejas.append(newBee)

    return
        
        

#GUI
"""
# IMAGENES
# BK
bg = pygame.image.load('bg.png')
# VACIO
vacio = pygame.image.load("vacio.png")
# Boton Pausa
p = pygame.image.load("p.png")
# Crea la ventana
qwirkle = pygame.display.set_mode((1300,800))
# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Nombre de la ventana
pygame.display.set_caption('Bees&Flowers by Sven&Rev')
reloj = pygame.time.Clock()

# FUENTE
font = pygame.font.SysFont("Minecraft", 20)
font2 = pygame.font.SysFont("Minecraft", 40)
font3 = pygame.font.SysFont("Minecraft", 10)
"""
