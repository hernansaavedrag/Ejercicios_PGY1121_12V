flag = True
while flag == True:
#while True:
    print("1. Calcular Primo")
    print("2. Salir")
    op = int(input())    

    if op == 1:
        i = 2
        num = int(input("Ingrese un número: "))
        cont = 0
        if num > 0:
            #for i in range(2,num):
            while( i < num):
                if num %i ==0:
                    cont = cont + 1
                i = i + 1
            if cont > 0:
                print("El número no es primo")
            else:
                print("El número es primo")
        else:
            print("El número debe ser mayor a cero")
    else:
        if op == 2:
            flag = False
            #break