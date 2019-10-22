from tkinter import *
import tkinter.font

def calculadorabtn():

    def sumar():
        r.set( float(n1.get()) + float(n2.get()) )
        borrar()

    def resta():
        r.set( float(n1.get()) - float(n2.get()) )
        borrar()

    def multiplicar():
        r.set( float(n1.get()) * float(n2.get()) )
        borrar()

    def dividir():
        r.set( float(n1.get()) * float(n2.get()) )
        borrar()
    
    def borrar():
        n1.set("")
        n2.set("")

    # Configuracion de la raiz
    root = Tk()
    root.config(bd=15)


    root.config(cursor="")
    root.config(bg="lightblue")
    root.config(bd=15)
    root.config(relief="ridge")




    n1 = StringVar()
    n2 = StringVar()
    r = StringVar()

    Label(root, text="Número 1").pack()
    Entry(root, justify="center", textvariable=n1).pack()

    Label(root, text="Número 2").pack()
    Entry(root, justify="center", textvariable=n2).pack()

    Label(root, text="Resultado").pack()
    Entry(root, justify="center", textvariable=r, state="disabled").pack()

    Label(root, text="").pack()  # Separador

    boton = Button(root, text="    +    ", activeforeground="#F50743", bg="#38EB5C", command=sumar, bd=3)
    boton.pack(side="left")
    boton = Button(root, text="    -    ", activeforeground="#F50743", bg="#38EB5C", command=resta, bd=3)
    boton.pack(side="left")
    boton = Button(root, text="    x    ", activeforeground="#F50743", bg="#38EB5C", command=multiplicar, bd=3)
    boton.pack(side="left")
    boton = Button(root, text="    /    ", activeforeground="#F50743", bg="#38EB5C", command=dividir, bd=3)
    boton.pack(side="top")


    root.mainloop()

calculadorabtn()
