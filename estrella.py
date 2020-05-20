import pygame
from libreria import *

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    origen = [ANCHO // 2, ALTO // 2]
    fin = False
    r = 270
    x = 38
    reloj = pygame.time.Clock()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

       
        ventana.fill(NEGRO)
        # Plano(ventana, origen)
        # Circulo(ventana, origen, 270)
        p = Heptagono(r, origen, x)

        Linea(ventana, p[0], p[2], BLANCO)
        Linea(ventana, p[2], p[4], BLANCO)
        Linea(ventana, p[4], p[6], BLANCO)
        Linea(ventana, p[6], p[1], BLANCO)
        Linea(ventana, p[1], p[3], BLANCO)
        Linea(ventana, p[3], p[5], BLANCO)
        Linea(ventana, p[5], p[0], BLANCO)
        Linea(ventana, p[0], p[2], BLANCO)
        Linea(ventana, p[2], p[4], BLANCO)
        Linea(ventana, p[4], p[6], BLANCO)
        Linea(ventana, p[6], p[1], BLANCO)
        Linea(ventana, p[1], p[3], BLANCO)
        Linea(ventana, p[3], p[5], BLANCO)
        Linea(ventana, p[5], p[0], BLANCO)
        x += 2

        reloj.tick(40)
        #refresco
        pygame.display.flip()