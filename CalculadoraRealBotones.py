from tkinter import *
from math import *

def calculadora():

    ventana=Tk()
    ventana.title("CALCULADORA                                          by: SAS")
    ventana.geometry("392x560")

    anchoBoton = 11
    altoBoton = 3

    ventana.configure(background="SkyBlue4")
    colorBoton = ("gray77")
    numerales = ("gray63")

    def btnClik(num):
        global operador
        operador = operador+str(num)
        inputText.set(operador)

    def clear():
        global operador
        operador=("")
        inputText.set("0")


    def operacion():
        global operador
        try:
            opera = str(eval(operador))
        except:
            clear()
            opera = ("ERROR")
        inputText.set(opera)

    inputText = StringVar()
    operador = ""
    clear()

    
    mensaje = Label(ventana, text="SASCULADORA", bg="LightSkyBlue4", width=18, height=2).place(x=17, y=12)


    #BOTONES
    boton0 = Button(ventana, text="0", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(0)).place(x=107, y=360)
    boton1 = Button(ventana, text="1", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(1)).place(x=17, y=300)
    boton2 = Button(ventana, text="2", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(2)).place(x=107, y=300)
    boton3 = Button(ventana, text="3", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(3)).place(x=197, y=300)
    boton4 = Button(ventana, text="4", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(4)).place(x=17, y=240)
    boton5 = Button(ventana, text="5", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(5)).place(x=107, y=240)
    boton6 = Button(ventana, text="6", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(6)).place(x=197, y=240)
    boton7 = Button(ventana, text="7", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(7)).place(x=17, y=180)
    boton8 = Button(ventana, text="8", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(8)).place(x=107, y=180)
    boton9 = Button(ventana, text="9", bg=numerales, width=anchoBoton, height=altoBoton, command=lambda:btnClik(9)).place(x=197, y=180)
    botonComa = Button(ventana, text=",", bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(".")).place(x=17, y=360)
    botonSuma = Button(ventana, text="+", bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("+")).place(x=287, y=180)
    botonResta = Button(ventana, text="-", bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("-")).place(x=287, y=240)
    botonC = Button(ventana, text="CE", bg=colorBoton, width=anchoBoton, height=altoBoton, command=clear).place(x=197, y=360)
    botonMultiplicacion = Button(ventana, text="x", bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("*")).place(x=287, y=360)
    botonDivision = Button(ventana, text="/", bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("/")).place(x=287, y=300)
    botonIgual = Button(ventana, text="=", bg=colorBoton, width=11, height=7, command=operacion).place(x=287, y=420)
    botonPi = Button(ventana, text="(", bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("(")).place(x=107, y=480)
    botonPd = Button(ventana, text=")", bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(")")).place(x=197, y=480)
    botonRaiz = Button(ventana, text="√" , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("sqrt")).place(x=197, y=420)
    botonPi = Button(ventana, text="Π" , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("pi")).place(x=17, y=480)
    botonExp = Button(ventana, text="EXP" , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("**")).place(x=17, y=420)
    botonResto = Button(ventana, text="%" , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik("%")).place(x=107, y=420)
    
    
    
    salida = Entry(ventana, font=("arial", 20, "bold"), width=22, textvariable=inputText, bd=20, insertwidth=4, bg="powder blue", justify="right").place(x=10, y=60)
    
    ventana.mainloop()

calculadora()
