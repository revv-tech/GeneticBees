#ABEJAS
import math
import random
"""
Estructura del DNA

Constaran de 26 bits

0-1-2: COLOR -> Color en RGB
3...12: DIRECCION -> Punto Cardinal
13...16: ANGULO -> Por ahora lo tendremos en 31 para tener 3 bits
17...23: DISTANCIA -> El maximo es 63 por lo que se utilizan 6 bits
24...26: TIPO DE RECORRIDO -> Hay tres tipos de recorridos. Se reservaron 4 combinaciones porque no se pueden de guardar 3, a la hora de hacer el cruce, crear la primera poblacion,...
        se intetara evitar la combinacion del [1,1]

"""
class Abeja:

    def __init__(self,dna):
        
        self.dna = dna
        self.color = (0,0,0)
        self.pos = (63,63)
        #LA DIRECCION SE MANEJARAN POR INTEGERS PARA A LA HORA DE HACER EL RECORRIDO IDENTIFICARLO
        self.direccion = 0
        #TIPO DE RECORRIDO: SE MANEJARAN CON INTEGERS ...""
        self.tipoRecorrido = 0
        self.distancia = 0
        self.anguloD = 0
        #CANTIDAD DE FLORES
        self.cantidadFlores = 0
        self.bitacora = ""
        self.polen = []
        self.chromosome = []
        self.grade = 0
        #DISTANCIA RECORRIDA AL BUSCAR FLORES
        self.distanciaRecorrida = 0
        
        

    def binaryListToDecimal(self,binary): 

        decimal = 0
        i = len(binary)-1
        j = 0
        
        while i >= 0:
            if binary[i]:
                decimal += 2**j
            i = i - 1
            j = j + 1
        
        return decimal

    
    def decodeColor(self):

        colorAbeja =[]
        
        for i in range(0,3):
            colorAbeja.append(self.dna[i])
            
        for i in range(0, len(colorAbeja)):

            if colorAbeja[i]:

                colorAbeja[i] = 255
                
        self.color = tuple(colorAbeja)

        #print(self.color)

    def decodeInfo(self):

        self.decodeColor()
        self.direccion = self.get360range(self.binaryListToDecimal(self.dna[3:12]))
        self.anguloD = self.binaryListToDecimal(self.dna[12:18])
        self.distancia = self.binaryListToDecimal(self.dna[18:24])
        self.tipoRecorrido = self.binaryListToDecimal(self.dna[24:26])
        
        return
    
    def get360range(self,n):
        if n <= 360:
            return n
        else:
            return self.get360range(n-360)
        
    def indexToAxis(self,i, j):

        if i < 64:

            X = -(63 - i)

        else:

            X = i - 63

        if j < 64:

            Y = -(63 - j)

        else:

            Y = j - 63

        return (X, Y)

    def printInfo(self):
        print()
        #print("Cadena DNA: ",self.dna)
        #print("Color: ",self.color)
        #print("Direccion: ", self.direccion)
        #print("Distancia: ", self.distancia)
        #print("Angulo de Desviacion: ",self.anguloD)
        #print("Tipo de Recorrido: ",self.tipoRecorrido)
        print("Cantidad de Flores Visitadas: ",self.cantidadFlores)
        print("Distancia Recorrida: ",self.distanciaRecorrida)
        print()
        return
    
    def busquedaFlores(self,listaFlores):

        #print("================================== ABEJA ==================================")
        #self.printInfo()
        availableFlowerList = []

        #PUNTOS QUE FORMAN EL RANGO DE BUSQUEDA
        
        #pointPrincipal = (round(math.cos(math.radians(self.direccion))* self.distancia),round(math.sin(math.radians(self.direccion))* self.distancia))
        

        secondPoint = (round(math.cos(math.radians(self.direccion + self.anguloD))* self.distancia),round(math.sin(math.radians(self.direccion + self.anguloD))* self.distancia))

        thirdPoint = (round(math.cos(math.radians(self.direccion - self.anguloD))* self.distancia),round(math.sin(math.radians(self.direccion - self.anguloD))* self.distancia))

        #print("Area: ",secondPoint,thirdPoint)

        #CHECKEA SI LA FLOR DE LA LISTA PERTENECE O NO AL TRIANGULO QUE FORMAN LOS PUNTOS DE ACUERDO AL PLANO
        for flor in listaFlores:

            location = flor.pos
        
            if self.isPointIn((0,0),secondPoint,thirdPoint,location):
                #flor.printInfo()
                availableFlowerList.append(flor)
        #TIPO DE RECORRIDO
        availableFlowerList = self.recorrido(availableFlowerList)
        #GET DISTANCIA
        self.distanciaRecorrida = self.getDistanceTraveled(availableFlowerList)
        #BUSQUEDA DE FLOR
        for available in availableFlowerList:

            self.getFlower(available)
            
        #self.printInfo()
        return
    
    def getDistanceTraveled(self,listaFlores):
        
        
        if listaFlores == []:

            return 0 
        

        totalD = 0

        for i in range(0,len(listaFlores)):

            j = i + 1

            if j == len(listaFlores):
                #print(totalD)
                return totalD
            else:
                
                totalD = totalD + self.distancePoints((listaFlores[i].pos,listaFlores[j].pos))
                
        return totalD
    
    def distancePoints(self,points):
       p0, p1 = points
       return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
            
        
    def isPointIn(self,p1,p2,p3,puntoBusqueda):
        
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        x3 = p3[0]
        y3 = p3[1]
        x  = puntoBusqueda[0]
        y  = puntoBusqueda[1]
          
        # Calculate area of triangle ABC 
        A = self.area (x1, y1, x2, y2, x3, y3) 
  
        # Calculate area of triangle PBC  
        A1 = self.area (x, y, x2, y2, x3, y3) 
      
        # Calculate area of triangle PAC  
        A2 = self.area (x1, y1, x, y, x3, y3) 
      
        # Calculate area of triangle PAB  
        A3 = self.area (x1, y1, x2, y2, x, y) 
      
        # Check if sum of A1, A2 and A3  
        # is same as A 
        if(A == A1 + A2 + A3): 
            return True
        else: 
            return False
    
    def area(self,x1, y1, x2, y2, x3, y3): 
  
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1)  + x3 * (y1 - y2)) / 2.0)


    #AGREGA LOS DATOS DE LA FLOR
    def getFlower(self,flower):

        if flower.color == self.color:

            #SUMA UNA FLOR
            self.cantidadFlores = self.cantidadFlores + 1

            #AGREGA EL POLEN
            self.polen.append(flower.dna)

            #AGREGAR A LA FLOR TODA POLEN DE LA ABEJA

            flower.addPolen(self.polen)

            return
        
        else:
            
            prob = random.randint(0, 100)

            if prob > 40:
                
                #SUMA UNA FLOR
                self.cantidadFlores = self.cantidadFlores + 1

                #AGREGA EL POLEN
                self.polen.append(flower.dna)
                
                #AGREGAR A LA FLOR TODA POLEN DE LA ABEJA
                flower.addPolen(self.polen)
                
            else:
                return

    def recorrido(self,flores):

        if self.tipoRecorrido == 2 or self.tipoRecorrido == 3:

            return flores
        
        elif self.tipoRecorrido == 1:

            #RECORRIDO POR ALTURA: SE ORDENA LA LISTA CON EL Y MAS CERCANO AL EJE X

            flores.sort(key = lambda y: y.pos[1])
            
            return flores

        elif self.tipoRecorrido == 0:

            #RECORRIDO POR ANCHURA: SE ORDENA LA LISTA CON EL X MENOR
            flores.sort(key = lambda X: X.pos[0])
            
            return flores
        
    
        
    
    
                

            
            
        
    

            
        
        
    
        
        
