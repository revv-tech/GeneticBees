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
generacionesAbejas = []
poblacionFlores = []
generacionesFlores = []
indiceGeneracion = 0


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

        while pos in flowersPos or pos == (63, 63):

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


def newFlowerGen(n):

    global poblacionFlores

    newGen = []
    
        
    for flower in poblacionFlores:
            
        newBorn = flower.reproduce()
        newBorn.gen = n
        newGen.append(newBorn)
    
    poblacionFlores = newGen
    

def newBeeGen(n):

    global poblacionAbejas

    beePop = createBeeList(poblacionAbejas)
    
    newGen = []

    while len(newGen) < len(poblacionAbejas):
        
        i = randint(0, len(beePop)-1)
        j = randint(0, len(beePop)-1)

        
        bee1 = beePop[i]
        bee2 = beePop[j]

        
        newBorns = crossBees(bee1, bee2)

        for newBorn in newBorns:
            newBorn.gen = n
            newGen.append(newBorn)
            
    poblacionAbejas = newGen


def crossBees(bee1, bee2):
   
    newBorns = []
    gen1 = bee1.dna
    gen2 = bee2.dna
    factorMut = 8
    newDNA1 = []
    newDNA2 = []
    cut = randint(0, len(gen1)-1)
    mutaedDNA1 = False
    mutaedDNA2 = False
    for i in range (0, cut):

        bit  = gen1[i]
        mutationValue = randint(1, 100)

        if mutationValue < factorMut:
            
            bit = mutate(bit)
            mutaedDNA1 = True
            
        newDNA1.append(bit)

    for i in range (cut, len(gen2)):

        bit  = gen2[i]
        mutationValue = randint(1, 100)

        if mutationValue < factorMut:
            
                bit = mutate(bit)
                mutaedDNA1 = True
                
        newDNA1.append(bit)

    for i in range(0, cut):

        bit  = gen2[i]
        mutationValue = randint(1, 100)

        if mutationValue < factorMut:
    
            bit = mutate(bit)
            mutaedDNA2 = True
        newDNA2.append(bit)
        

    for i in range (cut, len(gen1)):

        bit  = gen1[i]
        mutationValue = randint(1, 100)

        if mutationValue < factorMut:

            bit = mutate(bit)
            mutaedDNA2 = True

        newDNA2.append(bit)

    bee1 = Abeja(newDNA1)
    bee1.decodeInfo()
    bee2 = Abeja(newDNA1)
    bee2.decodeInfo()
    
    bee1.chromosome += [bee1,bee2]
    bee2.chromosome += [bee1,bee2]
    
    if mutaedDNA1:
        bee1.mutated = True
    if mutaedDNA2:
        bee2.mutated = True
    newBorns.append(bee1)
    newBorns.append(bee2)
    
            
    return newBorns


    
def createBeeList(beePopulation):

    beeList = []
    
    
        
    for bee in beePopulation:

        if len(beeList) == 1000:
        
            return beeList
            
        if bee.calificacion < 50:

            num = randint(1, 100)

            if num < 50:

                copyBee = bee
                beeList.append(copyBee)

        elif 50 <= bee.calificacion and bee.calificacion < 60:

            for i in range(0, 3):

                copyBee = bee
                beeList.append(copyBee)

        elif 60 <= bee.calificacion and bee.calificacion < 70:

            for i in range(0, 6):

                copyBee = bee
                beeList.append(copyBee)
                    
        elif 70 <= bee.calificacion and bee.calificacion < 80:

            for i in range(0, 12):

                copyBee = bee
                beeList.append(copyBee)

        elif 80 <= bee.calificacion and bee.calificacion < 90:

            for i in range(0, 24):

                copyBee = bee
                beeList.append(copyBee)

        elif 90 <= bee.calificacion and bee.calificacion <= 100:

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
bg = pygame.image.load('grass_2.png')
# IMAGENES
# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
# Crea la ventana
garden = pygame.display.set_mode((1300,740))

# Nombre de la ventana
pygame.display.set_caption('Bees&Flowers by Sven&Rev')
reloj = pygame.time.Clock()

fontNew = pygame.font.SysFont(None, 35)
panal = pygame.image.load("panal.png")

#MOSTRAR IMAGENES DE FLORES
def showFlowers():

    for i in range(0,127):
        for j in range(0,127):

            if searchPos((i,j),poblacionFlores):
                flower = searchPos((i,j),poblacionFlores)
                name = str(flower.color) + ".png"
                image = pygame.image.load(name)
                flower.decodeColor()
                flower.decodePos()
                pos = flower.index
                imageSetter(int(j*50/10),int(i*90/10),image)
            
    return
def showFlowersI(i):
    gen = generacionesFlores[i]
    for i in range(0,127):
        for j in range(0,127):

            if searchPos((i,j),gen):
                flower = searchPos((i,j),gen)
                name = str(flower.color) + ".png"
                image = pygame.image.load(name)
                flower.decodeColor()
                flower.decodePos()
                pos = flower.index
                imageSetter(int(j*50/10),int(i*90/10),image)
            
    return

def searchPos(pos,lista):

    for flor in lista:
        if pos == flor.index:
            return flor
        
    return False
# ACOMODAR IMAGENES
def imageSetter(x, y, name):
    garden.blit(name, (x, y))
 
def gui():
    indice = 0
    userText = ""
    userText1 = ""
    userText2 = ""
    loop = True
    global poblacionFlores
    global poblacionAbejas
    finish = False
    nF = 100
    nA = 100
    nGEN = 10
    nGenAux = nGEN
    genFlowerPop(nF)
    genAbejasGenerator(nA)
    busquedaFloresPop()
    
    nGEN = nGEN - 1
    inputRec_1 = pygame.Rect(700,50,140,32)
    inputRec_2 = pygame.Rect(1100,50,140,32)
    #inputRec_3 = pygame.Rect(1100,50,140,32)
    active1 = False
    active2 = False
    active3 = False
    while loop:
        
        
        text_surface = fontNew.render(userText,True,(255,255,255))
        text_surface1 = fontNew.render(userText1,True,(255,255,255))
        text_surface2 = fontNew.render(userText2,True,(255,255,255))
        
        garden.blit(bg, (0, 0))
        imageSetter(320,320,panal)
        
        pygame.draw.rect(garden,blanco,inputRec_1,2)
        pygame.draw.rect(garden,blanco,inputRec_2,2)
        #pygame.draw.rect(garden,blanco,inputRec_3,2)
        garden.blit(text_surface,(inputRec_1.x + 5,inputRec_1.y + 5))
        garden.blit(text_surface1,(inputRec_2.x + 5,inputRec_2.y + 5))
        #garden.blit(text_surface2,(inputRec_3.x + 5,inputRec_3.y + 5))
        
        if not finish:
            texto(300,650,"GENERACION #" + str(nGenAux-nGEN),90,blanco)
            showFlowers()
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputRec_1.collidepoint(event.pos):
                    active1 = True
                    active2 = False
                    active3 = False
                if inputRec_2.collidepoint(event.pos):
                    active1 = False
                    active2 = True
                    active3 = False
                    """
                if inputRec_3.collidepoint(event.pos):
                    active1 = False
                    active2 = False
                    active3 = True
                    """
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if indice >= 0:
                        indice += 1
                if event.key == pygame.K_LEFT:
                    indice -= 1
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        userText = userText[-1]
                    else:
                        userText += event.unicode

                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        userText1 = userText1[-1]
                    else:
                        userText1 += event.unicode
                        
                if active3:
                    if event.key == pygame.K_BACKSPACE:
                        userText2 = userText2[-1]
                    else:
                        userText2 += event.unicode
                if event.key == pygame.K_RETURN:
                    if userText != "" and userText1 != "":
                        numeroAbeja = int(userText)
                        gen = int(userText1)
                        textoAbeja(1000,200,25,blanco,getStadisticsBee(numeroAbeja,gen))
                    if userText != "" and userText1 == "":
                        gen = int(userText)
                        textoDatos(1000,200,25,blanco,getStadisticsGen(gen,nGenAux))
                        indice = gen
                    
                
        if nGEN > 0:
            nGEN = nGEN - 1
            
        #CREA NUEVAS GENERACIONES
        if nGEN > 0:
            
            generations(nGenAux - nGEN)
            printGensSta(poblacionAbejas,poblacionFlores,nGenAux-nGEN)
            
        
        if nGEN == 0:
            
            finish = True
            showFlowersI(indice)
            texto(300,650,"GENERACION #" + str(indice),90,blanco)
            #textoDatos(1000,200,25,blanco,getStadisticsGen(indice,nGenAux))
            #textoAbeja(1000,200,25,blanco,getStadisticsBee(75,6))
            #print(getStadisticsGen(4,nGenAux))
            #print(getStadisticsBee(75,6))
        texto(770,20,"NUMERO GENERACION Ab.",20,blanco)
        texto(1170,20,"NUMERO ABEJA",20,blanco)
        pygame.display.update()
        reloj.tick(1)
        
#LOOP GENERACIONES
#E: Cantidad de Generaciones
#S: No tiene
#D: Calcula la cantidad de generaciones el loop

def generations(n):
    
    global poblacionAbejas
    global poblacionFlores
    global generacionesAbejas
    global generacionesFlores
    
    generacionesAbejas = generacionesAbejas + [poblacionAbejas]
    
    generacionesFlores = generacionesFlores + [poblacionFlores]
    
    newFlowerGen(n)
    newBeeGen(n)
    #BUSQUEDA
    busquedaFloresPop()
    return

def getStadisticsBee(n,Gen):
    abeja = generacionesAbejas[Gen][n]
    return abeja.bitTa()


def getStadisticsGen(n,total):
    res = ["------------------------------------- GEN #" + str(n+1) + " -------------------------------------"]
    generacion = generacionesAbejas[n]
    genFlores = generacionesFlores[n]
    colorFav = []
    promedioDir = []
    promedioDis = []
    promedioAngD = []
    cantidadVi = []
    promCal = []
    cantMutadas = 0
    mayorFlores = []
    
    for bee in generacion:
        
        colorFav.append(bee.color)
        promedioDir.append(bee.direccion)
        promedioAngD.append(bee.anguloD)
        promedioDis.append(bee.distanciaRecorrida)
        promCal.append(bee.calificacion)
        cantidadVi.append(bee.cantidadFlores)
        
        if bee.mutated:
            cantMutadas += 1
    for flor in genFlores:
        mayorFlores.append(flor.color)
    
    res.append("El color favorito de la generacion fue: " + textColor(most_frequent(colorFav)))
    
    res.append("Promedio de direccion del recorrido fue: "+ textDireccion(promediarLista(promedioDir)))
    
    res.append("Promedio del angulo de desviacion fue: "+ str(promediarLista(promedioAngD))  )
    
    res.append("Promedio de las calificaciones de las abejas: "+ str(promediarLista(promCal)) )
    
    res.append("Promedio de la distancia recorrida: " + str(promediarLista(promedioDis)))
    
    res.append("Cantidad de Flores Mutadas: " + str(cantMutadas) )
    
    res.append("Cantidad Promedio de Flores Visitadas: "+ str(promediarLista(cantidadVi)))

    #res.append("-------FLORES-------")

    #res.append("Color mas comun: " + str(most_frequent(mayorFlores)))
    
    return res 
def printGensSta(generacion,genFlores,n):

    res = "------------------------------------- GEN #" + str(n) +"-------------------------------------"
    colorFav = []
    promedioDir = []
    promedioDis = []
    promedioAngD = []
    cantidadVi = []
    promCal = []
    cantMutadas = 0
    mayorFlores = []
    
    for bee in generacion:
        
        colorFav.append(bee.color)
        promedioDir.append(bee.direccion)
        promedioAngD.append(bee.anguloD)
        promedioDis.append(bee.distanciaRecorrida)
        promCal.append(bee.calificacion)
        cantidadVi.append(bee.cantidadFlores)
        
        if bee.mutated:
            cantMutadas += 1
            
    for flor in genFlores:
        mayorFlores.append(flor.color)
    
    res += "El color favorito de la generacion fue: " + str(most_frequent(colorFav)) + "\n"
    
    res += "Promedio de direccion del recorrido fue: "+ str(promediarLista(promedioDir))+ "\n" 
    
    res += "Promedio del angulo de desviacion fue: "+ str(promediarLista(promedioAngD)) + "\n" 
    
    res += "Promedio de las calificaciones de las abejas: "+ str(promediarLista(promCal)) + "\n" 
    
    res += "Promedio de la distancia recorrida: " + str(promediarLista(promedioDis)) + "\n"
    
    res += "Cantidad de Flores Mutadas: " + str(cantMutadas) + "\n"
    
    res += "Cantidad Promedio de Flores Visitadas: "+ str(promediarLista(cantidadVi))+ "\n"

    res += "-------FLORES-------" + "\n"

    res += "Color mas comun: " + str(most_frequent(mayorFlores))+ "\n"
    
    print(res)
    return
def textColor(color):

    if color == (0,0,0):

        return "Negro"

    elif color == (255,0,0):

        return "Rojo"

    elif color == (0,255,0):

        return "Verde"

    elif color == (0,0,255):

        return "Azul"

    elif color == (255,255,0):

        return "Morado"

    elif color == (0,255,255):

        return "Amarillo"

    elif color == (255,0,255):

        return "Rosado"

    elif color == (255,255,255):

        return "Blanco"

def textDireccion(angulo):

    if (angulo >= 0 and angulo < 30) or (angulo >= 330 and angulo <= 360):

        return "Este"

    elif angulo >= 30 and angulo < 60:

        return "Noreste"

    elif angulo >= 60 and angulo < 120:

        return "Norte"

    elif angulo >= 120 and angulo < 150:

        return "Noroeste"

    elif angulo >= 150 and angulo < 210:

        return "Oeste"

    elif angulo >= 210 and angulo < 240:

        return "Suroeste"

    elif angulo >= 240 and angulo < 300:

        return "Sur"

    elif angulo >= 300 and angulo < 330:

        return "Sureste"
        
        

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
 
    return sum/len(lista)
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 

def busquedaFloresPop():
    for bee in poblacionAbejas:
        bee.busquedaFlores(poblacionFlores)
        bee.adaptability()
    return
        
# Configuracion texto
#E:  Un string, un color, un numero
#S:  No tiene
#D:  Verifica la superficie en la que se escribira el texto

def texto_aux(texto,fuente,color):
     superficie = fuente.render(texto,True,color)
     return superficie, superficie.get_rect()

#E: Tres numeros, un color, un string
#S: Un texto
#D: Crea el texto
     
def texto(x,y,texto,tamano,color):
     font = pygame.font.SysFont(None, tamano)
     superficie,rectangulo = texto_aux(texto, font,color)
     rectangulo.center= ((x),(y))
     garden.blit(superficie,rectangulo)
     pygame.display.update()
     
def textoDatos(x,y,tamano,color,listaText):

    texto(x,y,listaText[0],tamano,color)
    texto(x,y+30,listaText[1],tamano,color)
    texto(x,y+60,listaText[2],tamano,color)
    texto(x,y+90,listaText[3],tamano,color)
    texto(x,y+120,listaText[4],tamano,color)
    texto(x,y+150,listaText[5],tamano,color)
    texto(x,y+180,listaText[6],tamano,color)
    texto(x,y+210,listaText[7],tamano,color)
    texto(x,y+240,listaText[8],tamano,color)
    texto(x,y+270,listaText[9],tamano,color)  
        
    return

def textoAbeja(x,y,tamano,color,listaText):

    texto(x,y,listaText[0],tamano,color)
    texto(x-15,y+30,listaText[1],tamano,color)
    texto(x,y+60,listaText[2],tamano,color)
    texto(x,y+90,listaText[3],tamano,color)
    texto(x,y+120,listaText[4],tamano,color)
    texto(x,y+150,listaText[5],tamano,color)
    texto(x,y+180,listaText[6],tamano,color)

    texto(x,y+210,listaText[7],tamano,color)
    texto(x,y+240,listaText[8],tamano,color)
    texto(x,y+300,listaText[9],tamano,color)
    texto(x,y+330,listaText[10],tamano,color)
    texto(x,y+360,listaText[11],tamano,color)
    texto(x,y+390,listaText[12],tamano,color)
    texto(x,y+420,listaText[13],tamano,color)
    
    return


gui()
    
