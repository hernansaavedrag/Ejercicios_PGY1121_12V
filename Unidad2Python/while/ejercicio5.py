i = 1
contCeros = 0
sumaPares = 0

while i <= 5:
    num = int(input("Ingrese un número: "))
    if num > 0 :
        contCeros = contCeros + 1
    
    if num%2==0 :
        sumaPares = sumaPares + num

    i = i + 1

print("hay ",contCeros, "números mayores a cero")
print("La suma de los números pares es: ", sumaPares)
