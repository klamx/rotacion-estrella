import pygame
import math

ANCHO = 900
ALTO = 700
origen = [ANCHO // 2, ALTO // 2]
BLANCO = [255, 255, 255]
NEGRO = [0, 0, 0]
AMARILLO = [255, 255, 0]
ROJO = [255, 0, 0]
AZUL = [0, 0, 255]
VERDE = [12, 221, 45]
MORADO = [206, 51, 255]

ANCHO = 1440
ALTO = 900
origen=[ANCHO//2,ALTO//2]
BLANCO = [255, 255, 255]
NEGRO = [0, 0, 0]
AMARILLO =[255,255,0]
ROJO = [255,0,0]
AZUL=[0,0,255]
VERDE = [12, 221, 45]

# v:ventana, o: origen, p: punto, d: tamanyo
def Punto(v, p, color=BLANCO, d = 2):
    pygame.draw.circle(v, color, p, d)

def Linea(v, inicio, final, color=BLANCO,d = 2):
    pygame.draw.line(v, color, inicio, final, d)

def Circulo(v, centro, radio, color=BLANCO, d = 2):
    pygame.draw.circle(v, color, centro, radio, d)

def Poligono(v,puntos,Color=BLANCO,d = 2):
    pygame.draw.polygon(v, Color, puntos, d)

# v: ventana, o: origen
def Plano(v, o, c = BLANCO):
    ox = o[0]
    oy = o[1]
    pygame.draw.line(v, c, [0, oy], [ANCHO, oy], 1)
    pygame.draw.line(v, c, [ox, 0], [ox, ALTO], 1)

# o: origen, p: punto
def Cart_A_Pantalla(o, p):
    px = p[0] + o[0]
    py = o[1] - p[1]
    return [px, py]

# r: radio
def polar_a_cartesiano(r, angulo):
    ar = math.radians(angulo)
    x = r * math.cos(ar)
    y = r * math.sin(ar)
    return [int(x), int(y)]

# p: punto, d: desplazamiento
def traslacion(p, d):
    xd = p[0] + d[0]
    yd = p[1] + d[1]
    return [xd, yd]

# o: origen, p: punto de pantalla
def rotacionHoraria(o, angulo, p):
    ar=math.radians(angulo)
    xp = (p[0] * math.cos(ar)) + (p[1] * math.sin(ar))
    yp = -(p[0] * math.sin(ar)) + (p[1] * math.cos(ar))
    return [int (xp), int (yp)]

# o: origen, p: punto de pantalla
def rotacionAntihoraria(o, angulo, p):
    ar=math.radians(angulo)
    xp = (p[0] * math.cos(ar)) - (p[1] * math.sin(ar))
    yp = (p[0] * math.sin(ar)) + (p[1] * math.cos(ar))
    return [int (xp), int (yp)]

#Pto fijo, p= punto a escalar; escal= a lo que se desea escalar
def escalapf(ptoFijo, p, escal):
    p1=[(-ptoFijo[0]+p[0]), (-ptoFijo[1]+p[1])]
    p1es=[((p1[0])*escal), ((p1[1])*escal)]
    p1e=[(ptoFijo[0]+p1es[0]), (ptoFijo[1]+p1es[1])]
    return p1e

#Pto fijo, p= punto a rotar; o = origen; r= angulo que se desea rotar
def rotacionpfah(ptoFijo, p, o, r):
    p1=[(-ptoFijo[0]+p[0]), (-ptoFijo[1]+p[1])]
    p1es=rotacionHoraria(o, r, p1)
    p1e=[(ptoFijo[0]+p1es[0]), (ptoFijo[1]+p1es[1])]
    return p1e

#Pto fijo, p= punto a rotar;0 = origen; r= angulo al que se desea rotar
def rotacionpfh(ptoFijo, p, o, r):
    p1=[(-ptoFijo[0]+p[0]), (-ptoFijo[1]+p[1])]
    p1es=rotacionAntihoraria(o, r, p1)
    p1e=[(ptoFijo[0]+p1es[0]), (ptoFijo[1]+p1es[1])]
    return p1e

a=51.4
def Heptagono(r, centro, a):
    p0=polar_a_cartesiano(r, 0+a)
    p1=polar_a_cartesiano(r, 51.4+a)
    p2=polar_a_cartesiano(r, 102.8+a)
    p3=polar_a_cartesiano(r, 154.2+a)
    p4=polar_a_cartesiano(r, 205.6+a)
    p5=polar_a_cartesiano(r, 257+a)
    p6=polar_a_cartesiano(r, 308.4+a)
    p0c=Cart_A_Pantalla(centro, p0)
    p1c=Cart_A_Pantalla(centro, p1)
    p2c=Cart_A_Pantalla(centro, p2)
    p3c=Cart_A_Pantalla(centro, p3)
    p4c=Cart_A_Pantalla(centro, p4)
    p5c=Cart_A_Pantalla(centro, p5)
    p6c=Cart_A_Pantalla(centro, p6)
    p=[p0c, p1c, p2c, p3c, p4c, p5c, p6c]
    return p
