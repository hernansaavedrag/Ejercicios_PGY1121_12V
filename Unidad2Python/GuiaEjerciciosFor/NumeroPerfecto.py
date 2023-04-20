num = int(input("Ingrese un número: "))
cont = 0
if num > 0:
    for i in range(1,num):
        if num %i ==0:
            cont = cont + i

    if cont == num:
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
else:
    print("El número debe ser mayor a cero")