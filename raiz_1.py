from tkinter import *


# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)


frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="")
frame.config(bg="red")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="orange")
root.config(bd=15)
root.config(relief="ridge")

# Finalmente bucle de la aplicación
root.mainloop()
