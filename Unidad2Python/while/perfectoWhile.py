i = 1
num = int(input("Ingrese un número: "))
cont = 0
if num > 0:
    #for i in range(1,num):
    while( i < num):
        if num %i ==0:
            cont = cont + i
        i = i + 1
    if cont == num:
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
else:
    print("El número debe ser mayor a cero")