

#tabla_hasta = int(input("Cantidad de valores a multiplicar: "))


valor = int(input("Ingrese valor de la tabla que quiere calcular: "))

# Iterar sobre un rango de números
for contador in range(1, 11):
    print(valor," x ",contador," = ", valor * contador)



#EJERCICIO
#CALCULAR LA SUMA DE LA FORMA 100 + 98 + 96 + ... + 1 

# 100 + 98 + 96 + 94 + 92 + ... + 2 = 2550

resultado = 0
for i in range(100, 0, -2):
    resultado = resultado + i
    # resultado += i
    if i != 2:
        print(str(i) + " + ", end ="")
    else:
        print(str(i), end="")

print(" = " + str(resultado))


#CALCULAR EL FACTORIAL DE UN NUMERO DADO

# ! 5 = 5 * 4 * 3 * 2 * 1 = 120 

