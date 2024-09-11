import datetime

def registrar_error():
    try:
        # Solicitar al usuario el tipo de error
        tipo_error = input("Ingrese el tipo de error (lectura de archivo, cálculo matemático, etc.): ")

        # Solicitar al usuario una descripción detallada del error
        descripcion_error = input("Ingrese una descripción detallada del error: ")

        # Obtener la fecha y hora actual
        fecha_hora_actual = datetime.datetime.now()

        # Formatear la fecha y hora para el archivo
        fecha_hora_formateada = fecha_hora_actual.strftime("%d-%m-%Y %H:%M:%S")

        # Preparar la información para el registro
        registro_error = f"{fecha_hora_formateada} | {tipo_error} | {descripcion_error}\n"

        # Abrir el archivo de errores en modo de escritura ("a")
        with open("errores.txt", "a") as archivo_errores:
            # Escribir el registro de error en el archivo
            archivo_errores.write(registro_error)

        print("Error registrado correctamente.")
    except Exception as e:
        print(f"Error al registrar el error: {e}")

# Ejecutar la función para registrar un error
registrar_error()
