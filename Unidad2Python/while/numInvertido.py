resp = "s"
while resp != "n":
    numIvertido = 0
    num = int(input("Ingrese un número: "))
    if num >=103 and num <=987:
        while num !=0:
            numIvertido = 10*numIvertido + num%10
            num = num //10 # // redondeo entero
    else:
        print("El número debe estar entre 103 y 987")
    print(numIvertido)
    resp = input("Desea ingresar nuevamente? s/n: " )
print("FIN")