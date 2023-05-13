# Solicitar al usuario su peso en kilogramos
peso = float(input("Ingrese su peso en kilogramos: "))

# Solicitar al usuario su altura en metros
altura = float(input("Ingrese su altura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (altura ** 2)

# Mostrar el resultado del IMC
print("Su índice de masa corporal (IMC) es:", imc)

# Determinar la clasificación del IMC
clasificacion = ""
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clasificacion = "Peso normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# Mostrar la clasificación del IMC
print("Clasificación:", clasificacion)
