def suma_dos_numeros(num1, num2):
    total = num1 + num2
    return total

n1 = int(input("Ingrese el primer número -> "))
n2 = int(input("Ingrese el segundo número -> "))

suma = suma_dos_numeros(n1, n2)
print("El resultado de sumar ",n1, " y ", n2, " es => ", suma)

numcoma1 = float(input("Ingrese valor con coma 1 = "))
numcoma2 = float(input("Ingrese valor con coma 2 = "))

total = suma_dos_numeros(numcoma1, numcoma2)

print("Sumé 2 valores con coma total = ", total)