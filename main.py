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

def genFlowerPop(maxPop):

    global poblacionFlores
    
    flowersPos = []

    for i in range(0, maxPop):


        dna = []
        n = randint(0, 7)
        
        i = randint(0, 127)
        j = randint(0, 127)
        pos = (i, j)

        #print(pos)
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
        newFlower.decodeFullInfo()
        poblacionFlores.append(newFlower)


    #for flor in poblacionFlores:

     #   print(flor.dna)


def newFlowerGen():

    global poblacionFlores

    newGen = []

    for flower in poblacionFlores:

        newBorn = flower.reproduce
        newGen.append(newBorn)

    poblacionFlores = newGen


def newBeeGen():

    global poblacionAbejas

    beePop = createBeeList(poblacionAbejas)
    
    newGen = []
    bee1 = beePop[i]
    bee2 = beePop[j]


    newBorns = crossBees(bee1, bee2)

    for newBorn in newBorns:
            
        newGen.append(newBorn)


    poblacionAbejas = newGen


def crossBees(bee1, bee2):
   
    newBorns = []
    gen1 = bee1.dna
    gen2 = bee2.dna

    newDna1 = []
    newDna2 = []
    cut = randint(0, len(gen1)-1)
        
    for i in range (0, cut):

        bit  = gen1[i]
        mutationValue = randint(1, 100)

        if mutationValue < 25:

            bit = mutate(bit)
                
        newDNA1.append(bit)

    for i in range (cut+1, len(gen2)):

        bit  = gen2[i]
        mutationValue = randint(1, 100)

        if mutationValue < 25:

                bit = mutate(bit)

        newDNA1.append(bit)

    for i in range(0, cut):

        bit  = gen2[i]
        mutationValue = randint(1, 100)

        if mutationValue < 25:

            bit = mutate(bit)
                
        newDNA2.append(bit)
        

    for i in range (cut+1, len(gen1)):

        bit  = gen1[i]
        mutationValue = randint(1, 100)

        if mutationValue < 25:

                bit = mutate(bit)

        newDNA2.append(bit)

    bee1 = Abeja(newDNA1)
    bee1.decodeInfo()
    bee2 = Abeja(newDNA1)
    bee2.decodeInfo()
    newBorns.append(bee1)
    newBorns.append(bee2)
            
    return newBorns

def adaptability(bee):

    print("Hala Madrid")

def createBeeList(beePopulation):

    beeList = []

    for bee in beeList:

        if bee.grade < 50:

            num = randint(1, 100)

            if num < 50:

                copyBee = bee
                beeList.append(copyBee)

        elif 50 <= bee.grade and bee.grade < 60:

            for i in range(0, 3):

                copyBee = bee
                beeList.append(copyBee)

        elif 60 <= bee.grade and bee.grade < 70:

            for i in range(0, 6):

                copyBee = bee
                beeList.append(copyBee)
                
        elif 70 <= bee.grade and bee.grade < 80:

            for i in range(0, 12):

                copyBee = bee
                beeList.append(copyBee)

        elif 80 <= bee.grade and bee.grade < 90:

            for i in range(0, 24):

                copyBee = bee
                beeList.append(copyBee)

        elif 90 <= bee.grade and bee.grade <= 100:

            for i in range(0, 48):

                copyBee = bee
                beeList.append(copyBee)

        return beeList
    

def mutate(bit):

    if bit:
        return 0
    else:
        return 1    
        
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
        newDir = randint(0, 511)
        #DISTANCIA
        newDist = randint(0, 63)
        #TIPO
        newTipo = randint(0, 3)
        #ANGULO DESVIACION
        newAngulo = randint(0,31)
        
        #MERGE DNA
        newBeeDNA = transBinaryFormat(newColor,3) + transBinaryFormat(newDir,9) + transBinaryFormat(newAngulo,6) + transBinaryFormat(newDist,6) + transBinaryFormat(newTipo,2)
        
        #NUEVA ABEJA
        newBee = Abeja(newBeeDNA)
        newBee.decodeInfo()
        #newBee.printInfo()
        newBee.busquedaFlores(poblacionFlores)
        poblacionAbejas.append(newBee)

#E: Dos Ints
#S: Una lista de bits
#D: Crea una lista con el numero en binario convertido
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
# BK
bg = pygame.image.load('grass.png')
# IMAGENES
# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
# Crea la ventana
garden = pygame.display.set_mode((1270,950))

# Nombre de la ventana
pygame.display.set_caption('Bees&Flowers by Sven&Rev')
reloj = pygame.time.Clock()

# FUENTE
font = pygame.font.SysFont("Minecraft", 20)
font2 = pygame.font.SysFont("Minecraft", 40)
font3 = pygame.font.SysFont("Minecraft", 10)
panal = pygame.image.load("panal.png")

#MOSTRAR IMAGENES DE FLORES
def showFlowers():

    for flower in poblacionFlores:
        name = str(flower.color) + ".png"
        image = pygame.image.load(name)
        flower.decodeColor()
        flower.decodePos()
        pos = flower.index
        imageSetter((pos[0]*10)*2,abs(pos[1]*10),image)
    return
        
# ACOMODAR IMAGENES
def imageSetter(x, y, name):
    garden.blit(name, (x, y))

def gui():
    
    loop = True
    global poblacionFlores
    global poblacionAbejas
    

    genFlowerPop(6000)
    genAbejasGenerator(500)

    genFlowerPop(3000)
    genAbejasGenerator(500)

    for bee in poblacionAbejas:

        bee.busquedaFlores(poblacionFlores)
        bee.printInfo()
        

    while loop:
        
        #garden.blit(bg, (0, 0))
        #showFlowers()
        #imageSetter(620,455,panal)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #if event.type == pygame.KEYDOWN:

        pygame.display.update()
        reloj.tick(1)


gui()
    
