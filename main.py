#PROGRA DE ABEJAS Y  FLORES
# Imports
import pygame


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

#GUI
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
