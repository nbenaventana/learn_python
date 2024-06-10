
# Ejemplo: División por cero
def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f"Resultado: {resultado}")
    except ZeroDivisionError as e:
        print(f"Error: No se puede dividir por cero")
    except TypeError as e:
        print(f"Error: Los tipos de datos no son compatibles para la división")

dividir(10, 2)  # Resultado: 5.0
dividir(10, 0)  # Error: No se puede dividir por cero
dividir("10", 2)  # Error: Los tipos de datos no son compatibles para la división
