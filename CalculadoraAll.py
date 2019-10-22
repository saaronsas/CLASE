import math

print("\n******************************")
print("*Bienvenidos a la calculadora*")
print("******************************\n\n")

def salir():
    while True:
        print("Hasta pronto...")
        break   


def calculadora():
    print("\nElija una de las siguientes opciones: \n")
    
    #opciones
    print("1. Sumar\n")
    print("2. Restar\n")
    print("3. Dividir\n")
    print("4. Multiplicar\n")
    print("5. Otras opciones\n")
    print("6. Salir\n")

    op = int(input(":   \n"))

    

    def suma():
        print("x + y\n")
        x = float(input("x:  "))
        y = float(input("y:  "))
        rst = x + y
        print(x,"+",y,"= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return suma()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
                
    def resta():
        print("x - y\n")
        x = float(input("x:  "))
        y = float(input("y:  "))
        rst = x - y
        print(x,"-",y,"= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return resta()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
                
    def division():
        print("x / y\n")
        x = float(input("x:  "))
        y = float(input("y:  "))
        rst = x / y
        print(x,"/",y,"= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return division()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
                
    def multiplicacion():
        print("x * y\n")
        x = float(input("x:  "))
        y = float(input("y:  "))
        rst = x * y
        print(x,"*",y,"= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return multiplicacion()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
                
    def potencias():
        print("x ** y\n")
        x = float(input("x:  "))
        y = float(input("y:  "))
        rst = x ** y
        print(x,"**",y,"= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return potencias()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
    def raiz():
        print("y^√x \n")
        x = float(input("x:  "))
        y = float(input("y:  "))
        rst = x ** 1/y
        print(y,"^√ ",x,"= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return raiz()
            elif opc is 2:
                return salir()
                break
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def seno():
        print("sen(x)\n")
        x = float(input(":   "))
        rst = math.sin(x)
        print("sen(",x,")= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return seno()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def coseno():
        print("cos(x)\n")
        x = float(input(":   "))
        rst = math.cos(x)
        print("cos(",x,")= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return coseno()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
    def tangente():
        print("tg(x)\n")
        x = float(input(":   "))
        rst = math.tan(x)
        print("tg(",x,")= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return tangente()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def arcoseno():
        print("asin(x)\n")
        x = float(input(":   "))
        rst = math.asin(x)
        print("asin(",x,")= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return arcoseno()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def arcocoseno():
        print("acos(x)\n")
        x = float(input(":   "))
        rst = math.acos(x)
        print("acos(",x,")= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return arcocoseno()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def arcotangente():
        print("atg(x)\n")
        x = float(input(":   "))
        rst = math.atan(x)
        print("atg(",x,")= ",rst,"\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return arcotangente()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    
    def ecuacion():
        print("Ax^2 + Bx + C = 0\n")
        A = float(input("A:   "))
        B = float(input("B:   "))
        C = float(input("C:   "))
        suma = B**2-4*A*C
        if(suma>=0):
            result1 = (-B + math.sqrt(suma)) / 2*A
            result2 = (-B - math.sqrt(suma)) / 2*A
            rst1= str(result1)
            rst2= str(result2)
            print(A,"x^2 + ",B,"x + ",C," = 0")
            print(rst1," y ",rst2,"\n")
        else:
            print("No se puede\n")
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return ecuacion()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
    #perimetros
    def ptriangulo():
        print("Perimetro Triangulo\n")
        print("a + b + c = Perimetro")
        a = float(input("a:   "))
        b = float(input("b:   "))
        c = float(input("c:   "))
        result = a+b+c
        print("Perimetro = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return ptriangulo()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def pcuadrado():
        print("Perimetro Rectangulo\n")
        print("2*a + 2*b = Perimetro")
        a = float(input("a:   "))
        b = float(input("b:   "))
        c = float(input("c:   "))
        result = 2*a+2*b
        print("Perimetro = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return pcuadrado()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def ppoligonoregular():
        print("Perimetro Poligono Regular\n")
        print("a * (numero de lados) = Perimetro")
        a = float(input("a:   "))
        num_lados = float(input("Numero de lados:   "))
        result = a*num_lados
        print("Perimetro = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return ppoligonoregular()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def pcirculo():
        print("Perimetro Circulo\n")
        print("2*π * r = Perimetro")
        r = float(input("r:   "))
        result = math.pi*r
        print("Perimetro = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return pcirculo()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    #areas
    def atriangulo():
        print("Area Triangulo\n")
        print("(b*h) / 2 = Area")
        b = float(input("b:   "))
        h = float(input("h:   "))
        result = (b*h)/2
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return atriangulo()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
                
    def arectangulo():
        print("Area Rectangulo\n")
        print("b * h = Area")
        b = float(input("b:   "))
        h = float(input("h:   "))
        result = b*h
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return arectangulo()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def arombo():
        print("Area Rombo\n")
        print("(D*d) / 2 = Area")
        x = float(input("D:   "))
        d = float(input("d:   "))
        result = (x*d)/2
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return arombo()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def aromboide():
        print("Area Romboide\n")
        print("b * h = Area")
        b = float(input("b:   "))
        h = float(input("h:   "))
        result = b*h
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return aromboide()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def atrapecio():
        print("Area Trapecio\n")
        print("((B+b)*h) / 2 = Area")
        b = float(input("b:   "))
        x = float(input("B:   "))
        h = float(input("h:   "))
        result = ((b+x)*h)/2
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return atrapecio()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def apoligono():
        print("Area Poligono 5 o +\n")
        print("(perimetro * apotema) / 2 = Area")
        p = float(input("Perimetro:   "))
        a = float(input("Apotema:   "))
        result = (p*a)/2
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return apoligono()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def acirculo():
        print("Area Circulo\n")
        print("π * r**2 = Area")
        r = float(input("r:   "))
        res = math.pi*(r**2)
        print("Area = ",res)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return pcirculo()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def asector():
        print("Area Sector Circular\n")
        print("(π * (r**2) * angulo) / 360º = Area")
        r = float(input("r:   "))
        a = float(input("Angulo:   "))
        result = (math.pi*(r**2)*a)/360
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return asector()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
                
    def asegmento():
        print("Area Segmento Circular\n")
        print("SectorCicular - TrianguloAOB = Area")
        c = float(input("Cuerda:   "))
        r = float(input("r:   "))
        a = float(input("Angulo:   "))
        m = math.sqrt((r**2)+((c/2)**2))
        sector = (math.pi*(r**2)*a)/360
        result = sector-m
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return asegmento()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    

    def acorona():
        print("Area Corona Circular\n")
        print("π * ((R**2)-(r**2)) = Area")
        r = float(input("r:   "))
        x = float(input("R:   "))
        result = math.pi * ((R**2)-(r**2))
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return acorona()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def atrapecio():
        print("Area Trapecio Circular\n")
        print("(π * ((R**2)-(r**2)) * angulo) / 360º = Area")
        r = float(input("r:   "))
        x = float(input("R:   "))
        a = float(input("Angulo:   "))
        result = (math.pi * ((R**2)-(r**2)) * a) / 360
        print("Area = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return atrapecio()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
                
    #volumenes
    def vtetaedro():
        print("Volumen Tetaedro\n")
        print("(√2) / 12 * a^3 = Volumen")
        a = float(input("a:   "))
        result = (math.sqrt(2)/12)*a**3
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vtetaedro()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def vcubo():
        print("Volumen Cubo\n")
        print("a^3 = Volumen")
        a = float(input("a:   "))
        result = a**3
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vcubo()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def voctaedro():
        print("Volumen Octaedro\n")
        print("(√2) / 3 * a^3 = Volumen")
        a = float(input("a:   "))
        result = (math.sqrt(2)/3)*a**3
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return voctaedro()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def vdodecaedro():
        print("Volumen Dodecaedro\n")
        print("(1/4) * (15+7*√5) * a**3 = Volumen")
        a = float(input("a:   "))
        result = (1/4)*(15+7*math.sqrt(5))*a**3
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vdodecaedro()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def vicosaedro():
        print("Volumen Icosaedro\n")
        print("(5/12) * (3+√5) * a**3 = Volumen")
        a = float(input("a:   "))
        result = (5/12)*(15+math.sqrt(5))*a**3
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vicosaedro()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def vprisma():
        print("Volumen Prisma\n")
        print("Abase * h = Volumen")
        a = float(input("Abase:   "))
        h = float(input("h:   "))
        result = a*h
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vprisma()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def vpiramide():
        print("Volumen Piramide\n")
        print("(Abase * h) / 3 = Volumen")
        a = float(input("Abase:   "))
        h = float(input("h:   "))
        result = (a*h)/3
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vpiramide()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def vcilindro():
        print("Volumen Cilindro\n")
        print(" π * r**2 * h = Volumen")
        r = float(input("r:   "))
        h = float(input("h:   "))
        result = math.pi*r*h
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vcilindro()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def vcono():
        print("Volumen Cono\n")
        print("(π * r**2 * h) / 3 = Volumen")
        r = float(input("r:   "))
        h = float(input("h:   "))
        result = math.pi*r*h/3
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vcono()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")

    def vesfera():
        print("Volumen Esfera\n")
        print(" (4/3) * π * r**3 = Volumen")
        r = float(input("r:   "))
        result = (math.pi*(r**3))*(4/3)
        print("Volumen = ",result)
        print("¿Deseas continuar?")
        print("1. SI")
        print("2. NO")
        print("3. Volver al menu de opciones")
        opc = int(input(":   \n"))
        while(opc<=3):
            if opc is 1:
                return vesfera()
            elif opc is 2:
                return salir()
            elif opc is 3:
                return calculadora()
            else:
                print("La introduccion no es valida")
    opcc=op
    while(opcc<=6):
        if opcc is 1:
            suma()
            break
            
        elif opcc is 2:
            resta()
            break
                
        elif opcc is 3:
            division()
            break

        elif opcc is 4:
            multiplicacion()
            break
            
        elif opcc is 5:
            #mas opciones
            print("Otras opciones: \n")
            print("1. Potencias\n") 
            print("2. Raices\n") 
            print("3. Trigonometria\n")
            print("4. Funciones\n")
            print("5. Areas, Perimetros y Volumenes\n")
            print("6. Salir\n")

            opm = int(input(":   \n"))
            while(opm<=6):
                if opm is 1:
                    potencias()
                    break
                elif opm is 2:
                    raiz()
                    break
                elif opm is 3:
                    print("Trigonometria: \n")
                    print("1. Seno\n")
                    print("2. Coseno\n")
                    print("3. Tangente\n")
                    print("4. Arcoseno\n")
                    print("5. Arcocoseno\n")
                    print("6. Arcotangente\n")
                    print("7. Volver al menu de opciones\n")
                    print("8. Salir\n")
                    oppm = int(input(":   \n"))
                    while(oppm<=8):
                        if oppm is 1:
                            seno()
                            break
                        elif oppm is 2:
                            coseno()
                            break
                
                        elif oppm is 3:
                            tangente()
                            break

                        elif oppm is 4:
                            arcoseno()
                            break
                
                        elif oppm is 5:
                            arcocoseno()
                            break

                        elif oppm is 6:
                            arcotangente()
                            break
                        elif oppm is 7:
                            return calculadora()
                            break
                        elif oppm is 8:
                            return salir()
                            break
                        else:
                            print("Introduzca algo valido: ")
                    break
                elif opm is 4:
                    ecuacion()
                    break
                elif opm is 5:
                    print("Areas, Perimetros y Volumenes: \n")
                    print("1. Perimetros")
                    print("2. Areas")
                    print("3. Volumenes")
                    print("4. Volver al menu de opciones")
                    print("5. Salir")
                    apv = int(input(":   \n"))
                    while(apv<=5):
                        if apv is 1:
                            print("Perimetros:")
                            print("1. Triangulos")
                            print("2. Rectangulos")
                            print("3. Poligonos regulares")
                            print("4. Circulo")
                            print("5. Volver al menu de opciones")
                            print("6. Salir")
                            apvp = int(input(":   \n"))
                            while(apva<=9):
                                if apva is 1:
                                    ptriangulo()
                                    break
                                elif apva is 2:
                                    pcuadrado()
                                    break
                                elif apva is 3:
                                    ppoligonoregular()
                                    break
                                elif apva is 4:
                                    pcirculo()
                                    break
                                elif apva is 5:
                                    return calculadora()
                                    break
                                elif apva is 6:
                                    return salir()
                                    break
                                else:
                                    print("Introduzca algo valido: ")
                        elif apv is 2:
                            print("Areas:")
                            print("1. Triangulo")
                            print("2. Rectangulo")
                            print("3. Rombo")
                            print("4. Romboide")
                            print("5. Trapecio")
                            print("6. Poligono 5 o +")
                            print("7. Circulo")
                            print("8. Volver al menu de opciones")
                            print("9. Salir")
                            apva = int(input(":   \n"))
                            while(apva<=9):
                                if apva is 1:
                                    atriangulo()
                                    break
                                elif apva is 2:
                                    arectangulo()
                                    break
                                elif apva is 3:
                                    arombo()
                                    break
                                elif apva is 4:
                                    aromboide()
                                    break
                                elif apva is 5:
                                    atrapecio()
                                    break
                                elif apva is 6:
                                    apoligono()
                                    break
                                elif apva is 7:
                                    print("Areas del Circulo")
                                    print("1. Circulo")
                                    print("2. Sector circular")
                                    print("3. Segmento circular")
                                    print("4. Corona circular")
                                    print("5. Trapecio circular")
                                    print("6. Volver al menu de opciones")
                                    print("7. Salir")
                                    apvac = int(input(":   \n"))
                                    while(apvac<=7):
                                        if apvac is 1:
                                            acirculo()
                                            break
                                        elif apvac is 2:
                                            asector()
                                            break
                                        elif apvac is 3:
                                            asegmento()
                                            break
                                        elif apvac is 4:
                                            acorona()
                                            break
                                        elif apvac is 5:
                                            atrapecio()
                                            break
                                        elif apvac is 6:
                                            return calculadora()
                                            break
                                        elif apvac is 7:
                                            return salir()
                                            break
                                        else:
                                            print("Introduzca algo valido: ")
                                elif apva is 8:
                                    return calculadora()
                                    break
                                elif apva is 9:
                                    return salir()
                                    break
                                else:
                                    print("Introduzca algo valido: ")
                                break
                        elif apv is 3:
                            print("Volumenes:")
                            print("1. Tetaedro")
                            print("2. Cubo")
                            print("3. Octaedro")
                            print("4. Dodecaedro")
                            print("5. Icosaedro")
                            print("6. Prisma")
                            print("7. Ortoedro")
                            print("8. Piramide")
                            print("9. Cilindro")
                            print("10. Cono")
                            print("11. Esfera")
                            print("12. Volver al menu de opciones")
                            print("13. Salir")
                            apvv = int(input(":   \n"))
                            while(apvv<=15):
                                if apvv is 1:
                                    vtetaedro()
                                    break
                                elif apvv is 2:
                                    vcubo()
                                    break
                                elif apvv is 3:
                                    voctaedro()
                                    break
                                elif apvv is 4:
                                    vdodecaedro()
                                    break
                                elif apvv is 5:
                                    vicosaedro()
                                    break
                                elif apvv is 6:
                                    vprisma()
                                    break
                                elif apvv is 7:
                                    vortoedro()
                                    break
                                elif apvv is 8:
                                    vpiramide()
                                    break
                                elif apvv is 9:
                                    vcilindro()
                                    break
                                elif apvv is 10:
                                    vcono()
                                    break
                                elif apvv is 11:
                                    vesfera()
                                    break
                                elif apvv is 12:
                                    return calculadora()
                                    break
                                elif apvv is 13:
                                    return salir()
                                    break
                                else:
                                    print("Introduzca algo valido: ")
                                break
                        elif apv is 4:
                            return calculadora()
                            break
                        elif apv is 5:
                            return salir()
                            break
                        else:
                            print("Introduzca algo valido: ")
                        break
                elif opm is 6:
                    return salir()
                    break
                else:
                    print("Introduzca algo valido: ")
                break
            break      

        elif opcc is 6:
            print("Hasta pronto...")
            break

        else:
            print("Introduzca algo valido: ")
        
    
    
calculadora()    


