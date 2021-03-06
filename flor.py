#FLOR
from random import randint
# La posición constará de 14 bits,
# En tras palabras, 2 cadenas de 7 bits cada una
# esto para generar numero entre 0 y 127
# ya que el tamaño de la matriz de flores es de 127x127

# El color constará de 3 bits, ya que son suficientes
# para hacer 8 combinaciones que son la cantidad total
# colores que podrán tener las flores

# Los primeros 7 bits son de las posicion i,
# los siguientes 7 bits son de la posicion j
# y los siguientes 3 bits son del color
# Estos estarán en el DNA
#[1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0]

class Flor:
    
    def __init__(self, dna):
        
        self.dna = dna
        self.color = (0, 0, 0)
        self.pos = (63, 62)
        self.index = (0, 0)
        self.polen = []
        self.chromosome = []
        self.bitacora = ""
        self.cantidadAbejas = 0

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
    
    def decodePos(self):

        I = self.binaryListToDecimal(self.dna[0:6])
        J = self.binaryListToDecimal(self.dna[7:14])

        self.index = (I,J)

        self.pos = self.indexToAxis(I, J)
            
    
    
    def decodeColor(self):

        colorFlor =[]
        
        for i in range(14,17):
            
            colorFlor.append(self.dna[i])
            
        for i in range(0, len(colorFlor)):

            if colorFlor[i]:

                colorFlor[i] = 255
                
        self.color = tuple(colorFlor)


    def reproduce(self):

        if self.polen == []:

            #Algoritmo usado para generar una flor totalmente random
            return self.randomFlower()


        
        else:

            indexX = randint(0, len(self.polen)-1)

            newDNA = []
            
            genX = self.polen[indexX]
            genY = self.dna

            cut = randint(0, len(genX)-1)

            for i in range (0, cut):

                bit  = genX[i]
                mutationValue = randint(1, 100)

                if mutationValue < 25:

                    bit = self.mutate(bit)

                newDNA.append(bit)

            for i in range (cut, len(genY)):

                bit  = genY[i]
                mutationValue = randint(1, 100)

                if mutationValue < 25:

                    bit = self.mutate(bit)

                newDNA.append(bit)

            flower = Flor(newDNA)
            flower.chromosome.append(genX)
            flower.chromosome.append(genY)
            
            return flower

    def randomFlower(self):

        dna = []
        n = randint(0, 7)
        flowersPos = []
        i = randint(0, 127)
        j = randint(0, 127)
        pos = (i, j)
        
        while pos in flowersPos or pos == (63, 63):

            i = randint(0, 127)
            j = randint(0, 127)
            pos = (i, j)
        
            flowersPos.append(pos)
        
        genI = self.transBinaryFormat(i,7)
        genJ = self.transBinaryFormat(j,7)
        genColor = self.transBinaryFormat(n,3)

        dna = genI + genJ + genColor
        newFlower = Flor(dna)
        newFlower.decodeFullInfo()
        return newFlower

        
    def mutate(self,bit):

        if bit:
            return 0
        else:
            return 1
    
    #E: Dos Ints
    #S: Una lista de bits
    #D: Crea una lista con el numero en binario convertido
    def transBinaryFormat(self,data,rangeBits):
        
        bitChain = self.decimalToBinary(data)
        dnaChain = []

        if len(bitChain) < rangeBits:
            for i in range(0, rangeBits-len(bitChain)):
                dnaChain.append(0)
                    
        for bit in bitChain:
                
            dnaChain.append(int(bit))
        
        return dnaChain
    #CONVERSOR
    #E: Un numero
    #S: Un numero binario
    #D: Convierte el numero dado en binario
    def decimalToBinary(self,n):  
        return bin(n).replace("0b", "")
    def binaryToDecimal(self,binary): 
          
        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal


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

    def addPolen(self,listPolen):

        for pol in listPolen:
            self.polen.append(pol)

        return
        
    def decodeFullInfo(self):
        self.decodePos()
        self.decodeColor()
        return
    
    def printInfo(self):
        print()
        print("Color: ",self.color)
        print("Index: ",self.index)
        print("Pos: ",self.pos)
        print("Lista Polen: ",self.polen)
        print()
        return

        

    

        
        
    

