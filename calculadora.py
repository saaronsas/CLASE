while True:
    print("Elige una de las siguientes opciones: ")
    
    print("'Sumar'")
    
    print("'Restar'")
    
    print("'Multiplicar'")
    
    print("'Dividir'")

    print("'Salir'")
    

    ui = input(": ")

    if ui == "Salir":
        break

    elif ui == "Sumar":
        num1 = float(input("Introduzca su primer numero: "))
        num2 = float(input("Introduzca su segundo numero: "))
        result = str(num1 + num2)
        print("La respuesta es " + result)
        
    elif ui == "Restar":
        num1 = float(input("Introduzca su primer numero: "))
        num2 = float(input("Introduzca su segundo numero: "))
        result = str(num1 - num2)
        print("La respuesta es " + result)
        
    elif ui == "Multiplicar":
        num1 = float(input("Introduzca su primer numero: "))
        num2 = float(input("Introduzca su segundo numero: "))
        result = str(num1 * num2)
        print("La respuesta es " + result)
        
    elif ui == "Dividir":
        num1 = float(input("Introduzca su primer numero: "))
        num2 = float(input("Introduzca su segundo numero: "))
        result = str(num1 / num2)
        print("La respuesta es " + result)
        
    else:
        print("Es necesario introducir alguna opcion")
