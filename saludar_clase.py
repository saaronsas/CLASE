def saludar():
    nombre = input("¿Cual es tu nombre? ")
    print(f"Me alegro de conocerle, {nombre}")
    print("¿Que le gustaria 'saludar' o 'despedirse' ? ")

    funcion = input(": ")
    if funcion == "despedirse" or "Despedirse":
        print(f"Que pase un buen dia, sr.{nombre}")
        break
    
    elif funcion == "saludar" or "Saludar":
        print(f"Me alegro de saludarle, sr.{nombre}")
    
    else:
        print("La funcion que ha introducida no es correcta por favor intentelo de nuevo")
       

saludar()    
