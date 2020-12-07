#ABEJAS
import math
"""
Estructura del DNA

Constaran de 20 bits

0-1-2: COLOR -> Color en RGB
3-4-5: DIRECCION -> Punto Cardinal
6...11: Angulo -> Por ahora lo tendremos en 31 para tener 3 bits
12...17: Distancia -> El maximo es 63 por lo que se utilizan 6 bits
18..20: Tipo de Recorrido -> Hay tres tipos de recorridos. Se reservaron 4 combinaciones porque no se pueden de guardar 3, a la hora de hacer el cruce, crear la primera poblacion,...
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
        self.cantidadFlores = 0
        self.binnacle = ""
        self.polen = []
        self.chromosome = []
        
        

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
        self.direcccion = self.binaryListToDecimal(self.dna[3:6])
        self.anguloD = self.binaryListToDecimal(self.dna[6:12])
        self.distancia = self.binaryListToDecimal(self.dna[12:18])
        self.tipoRecorrido = self.binaryListToDecimal(self.dna[18:20])
        
        return

    def indexToAxis(i, j):

        if i < 64:

            X = -(63 - i)

        else:

            X = i - 64

        if j < 64:

            Y = 63 - j

        else:

            Y = -(i - 63)

        return (X, Y)

    def printInfo(self):
        print()
        print("Cadena DNA: ",self.dna)
        print("Color: ",self.color)
        print("Direccion: ", self.direccion)
        print("Distancia: ", self.distancia)
        print("Angulo de Desviacion: ",self.anguloD)
        print("Tipo de Recorrido: ",self.tipoRecorrido)
        print("Cantidad de Flores Visitadas: ",self.cantidadFlores)
        print()
        return
    
    def busquedaFlores(self,listaFlores):    

        point = [round(math.cos(math.radians(self.anguloD))* math.sqrt(distancia)),round(math.sin(math.radians(self.anguloD))* math.sqrt(distancia))]

        thirdPoint = getNearerSide(point)

        for flor in listaFlores:

            if flor.pos 
            
            

        
        
        return

    def pointInRange(p1,p2):
        
        return
    def getNearerSide(self,point):

        if 90 - self.anguloD <= 45:
            return (point[0],0)
        
        else:
            return (0,point[1])
        
    def transformPoint(self,point):

        #NORTE
        if self.direccion == 0:
            return
        #SUR
        elif self.direccion == 4:
            return
        #ESTE
        elif self.direccion == 2:
            return
        #OESTE
        elif self.direccion == 6:
            return
        #SURESTE
        elif self.direccion == 3:
            return [point[0]] + [point[1] * -1]
        #SUROESTE
        elif self.direccion == 5:
            return [point[0] * -1 ] + [point[1] * -1]
        #NOROESTE
        elif self.direccion == 7:
            return [point[0] * -1 ] + [point[1]]
        #NORESTE
        else:
            return point
        
        
    
        
        
