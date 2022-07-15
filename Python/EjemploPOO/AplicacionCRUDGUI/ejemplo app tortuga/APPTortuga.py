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
        y += longitudPedazoLinea
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
#crear ventana donde akojaremos la tortuga
tortuga.setup(800,600,0,0)#ver area de trabajo
tortuga.screensize(800,600)#area de trabajo
tortuga.title("Dibujo Figuras Geometricas")#ponerle titulo a el area de trabajo
tortuga.showturtle()#mostrar tortuga
#interaccion consola
saludo()
#Mainloop: procedimientos que muestran el comportamiento del objeto tortuga
mainloop = True
while mainloop:
     #Solicitar a la interfaz la selección de una opción
    opcion = FormularioMenuAppTortuga()

    #Si Dibujado de líneas discontinuas fue seleccionado
    if opcion == 1:       

        #Reportar en consola procedimiento del objeto
        mensaje("->Dibujado de Líneas Discontinuas")
        
        #Procedimiento ralizando cambios de estado en el objeto        
        longitudPedazoLinea = 15
        tortuga.clear()
        LineaHorizontalContinua(tortuga,longitudPedazoLinea)        
        tortuga.clear()
        lineaDiagonalDiscontinua(tortuga,longitudPedazoLinea,x=-100,y=-100)        
        tortuga.clear()
        LineaHorizontalContinua(tortuga,longitudPedazoLinea=5,x=-300)
              
    elif opcion == 2:
        mensaje("->Dibujando Polígono Irregular de 4 Lados sin Relleno")             
        tortuga.clear()
        poligonoConvexo4Lados(tortuga)#Crear un polígono convexo irregular 4 lados (paso a paso)   
                      
    elif opcion == 3:
        mensaje("->Dibujando Polígono Irregular de 4 Lados con Relleno")       
        tortuga.clear()
        poligonoConvexo4LadosRelleno(tortuga)#Crear un polígono convexo irregular 4 lados (paso a paso)
        
    elif opcion == 4:
        mensaje("->Dibujando Polilínea Coordenadas por Consola")        

        #Polilínea (polígono que se va generando) con coordenadas ingresadas por el usuario
        tortuga.clear()
        tortuga.goto(0,0)
        recogiendoCoordenadas = True
        relleno = input('Rellenar polilínea? (s)').lower() == 's'
        if relleno:
            tortuga.begin_fill()
            tortuga.fillcolor('red')
        colores = ['blue','orange','red','black','yellow','cyan']
        while(recogiendoCoordenadas):
            x,y = RecojerCordenadasTeclado()
            tortuga.goto(x,y)
            tortuga.dot(10, colores[ random.randint(0,len(colores)-1) ] )
            recogiendoCoordenadas = ControlParada()
        if relleno:
            tortuga.end_fill()   

    #Si la opcíon de salida fue seleccionadA por el usuario en el menú    
    elif opcion == 5:
        
        #Solicitar a la interfaz mostrar el mensaje de cierre        
        despedida()
        input('Presione cualquier tecla para cerrar ventana.')

        #Finalización:
        #Cerrar la ventana
        #Terminar procesos con tortuga
        tortuga.bye()
        
        #Terminar el mainloop de la aplicación
        mainloop = False
    
    else:
        #Solicitar a la interfaz mostrar el mensaje
        mensaje("Opción inválida!")



    