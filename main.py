#PROGRA DE ABEJAS Y  FLORES
# Imports
import pygame
from random import randint
from flor import Flor


pygame.init()


#CORREGIR LA MATRIZ CON LAS STRUCTS
# E: Dos ints
# S: Una Matriz
# D:Crea una matriz con la cantidad de C y F que se le pase
def generadorMatriz(filas, columnas):
    M = []
    for i in range(columnas):
        columna = [0]*filas
        M.append(columna)

    return M


#MATRIZ
mapa = generadorMatriz(128,128)


#POBLACION INICIAL
poblacionAbejas = []
poblacionFlores = []


#CONVERSOR
#E: Un numero
#S: Un numero binario
#D: Convierte el numero dado en binario
def decimalToBinary(n):  
    return bin(n).replace("0b", "")

    
#CREADOR DE ABEJAS
"""
ESTRUCTURA:


"""
#E:
#S:
#D:

def genFlowerPoblation(maxPop):

    for i in range(0, maxPop):

        dna = []
        n = randint(0, 7)
        i = randint(0, 127)
        j = randint(0, 127)
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

        print(dna)
        poblacionFlores.append(Flor(dna))


    #for flor in poblacionFlores:

     #   print(flor.dna)

                       


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
