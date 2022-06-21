from turtle import *
#Librería para funciones aleatorias
import random
import turtle
from InterfazConsola import  *
#Procedimientos trabajando con el objeto tortuga: comportamiento
def LineaHorizontalContinua (tortuga,longitudPedazoLinea=5,x=0,y=0,numerosRayas=10):
    alternador = True
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.pendown()
    for _ in range(numerosRayas):
        tortuga.goto(x+longitudPedazoLinea,y)
        x += longitudPedazoLinea
        #y += longitudPedazoLinea
        if alternador: 
            tortuga.penup()
            alternador = False
        else:
            tortuga.pendown()
            alternador = True
    #retornar al origen
    tortuga.penup()
    tortuga.goto(0,0)
def lineaDiagonalDiscontinua(tortuga,longitudPedazoLinea=5,x=0,y=0,numeroRayas=10):
    alternador = True
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.pendown()
    for _ in range(numeroRayas):
        tortuga.goto(x+longitudPedazoLinea,y+longitudPedazoLinea)
        x += longitudPedazoLinea
        y += longitudPedazoLinea
        if alternador:
            tortuga.penup()
            alternador = False
        else:
            tortuga.pendown()
            alternador = True        
    #Retornar al origen
    tortuga.penup()
    tortuga.goto(0,0)
    
def poligonoConvexo4LadosRelleno(tortuga):
    tortuga.begin_fill()
    tortuga.fillcolor('red')
    tortuga.goto(0,0)
    tortuga.pendown()
    tortuga.goto(100,50)
    tortuga.dot(10,'blue')#También: rgb -> reed green blue -> 255,255,255
    tortuga.goto(100,-50)
    tortuga.dot(10,'red')
    tortuga.goto(50,-50)
    tortuga.dot(10,'orange')
    tortuga.goto(0,0)
    tortuga.dot(10,'black')
    tortuga.end_fill()

def poligonoConvexo4Lados(tortuga):    
    tortuga.goto(0,0)
    tortuga.pendown()
    tortuga.goto(100,50)
    tortuga.dot(10,'blue')#También: rgb -> reed green blue -> 255,255,255
    tortuga.goto(100,-50)
    tortuga.dot(10,'red')
    tortuga.goto(50,-50)
    tortuga.dot(10,'orange')
    tortuga.goto(0,0)
    tortuga.dot(10,'black')
#objeto tipo tortuga
tortuga = turtle
#iniciar interaccion con la interfaz grafica

    