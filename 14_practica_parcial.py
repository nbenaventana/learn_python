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


#Ejemplo de caso en parcial ---------------------------------------------
producto = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ahora ingresa el porcentaje a aplicar: % "))
calculoDescuento = (float(descuento*producto)/100)

if(descuento >=1 and descuento <=10):
    print("Es un descuento estándar.")
    print("El descuento es de: $", calculoDescuento)
    precioFinal = (producto - calculoDescuento)
    print("El precio final es: $",precioFinal)
elif(descuento >=11 and descuento <=25):
    print("Es un descuento medio.")
    print("El descuento es de: $", calculoDescuento)
    precioFinal = (producto - calculoDescuento)
    print("El precio final es: $",precioFinal)
elif(descuento >=26 and descuento <=50):
    print("Es un gran descuento.")
    print("El descuento es de: $", calculoDescuento)
    precioFinal = (producto - calculoDescuento)
    print("El precio final es: $",precioFinal)
elif(descuento >50):
    print("Es un descuento increíble.")
    print("El descuento es de: $", calculoDescuento)
    precioFinal = (producto - calculoDescuento)
    print("El precio final es: $",precioFinal)
else:
    print("Sin descuento.")
    print("El precio final es: $",producto)