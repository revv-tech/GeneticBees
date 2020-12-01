#FLOR

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
        self.pos = (63, 63)
        self.index = (0, 0)


    def decodePos(dna):

        genPosI = []
        genPosJ = []

        for i in range (0, 7):

            genPosI += dna[i]

        for i in range (7, 14):

            genPosJ += dna[i]

        binI = int(''.join(map(str,genPosI)))
        binJ = int(''.join(map(str,genPosj)))

        I = binaryToDecimal(binX)
        J = binaryToDecimal(binY)

        self.index[0] = I
        self.index[1] = J

        self.pos = indexToAxis(I, J)
            

    
    def decodeColor(dna):

        genColor = []

        for i in range(14, 17):

            genColor.append(dna[i])

        for i in range(0, len(genColor)):

            if genColor[i]:

                self.color[i] = 255

        print(self.color)

            
    def binaryToDecimal(binary): 
          
        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal


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
        

        

    

        
        
    

