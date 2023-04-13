import pygame #importa el modulo pygame
import sys

ancho = 300 #define el ancho de la ventana
alto = 500 #define el alto de la ventana
pygame.init() #instancia el modulo
ventana = pygame.display.set_mode((ancho,alto)) #le da las medidas a la ventana
pygame.display.set_caption("proyecto") #le pone un titulo a la ventana

while True:
    ventana.fill([255,255,255])
    pygame.display.update()
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            sys.exit()