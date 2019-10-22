def reto():
    
    num = int(input("Introduzca su numero: "))

    i = 1
    while i <= num:

        if(i == 1):
            print("1 : es IMPAR y PRIMO")
            
        elif(i == 2):
            print("2 : es PAR y PRIMO")
            
        elif(i == 3):
            print("3 : es IMPAR y PRIMO")
            
        else:
            if(i % 2 == 0):
                a = i
                b = int(a/2) + 1
                d = b-1

                for j in range(2,b):
                    c = a % j

                    if c == 0:
                        print(i,": es PAR y NO PRIMO ")
                        break

                    elif j>=d:
                        print(i,": es PAR y PRIMO ")
                        break
                        
                    else:
                        j=j+1

            else:
                a = i
                b = int(a/2) + 1
                d = b-1

                for j in range(2,b):
                    c = a % j

                    if c == 0:
                        print(i,": es IMPAR y NO PRIMO ")
                        break

                    elif j>=d:
                        print(i,": es IMPAR y PRIMO ")
                        break
                        
                    else:
                        j=j+1
        i = i + 1

reto()


            
            
