num = int(input("Ingrese un número: "))
cont = 0
if num > 0:
    for i in range(2,num):
        if num %i ==0:
            cont = cont + 1

    if cont > 0:
        print("El número no es primo")
    else:
        print("El número es primo")
else:
    print("El número debe ser mayor a cero")