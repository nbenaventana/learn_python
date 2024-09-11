import csv

def analizar_ventas(archivo_csv):
    try:
        # Abrir el archivo CSV en modo lectura
        with open(archivo_csv, "r") as archivo:
            # Crear un lector CSV
            lector_csv = csv.reader(archivo)

            # Omitir la primera fila (encabezados)
            next(lector_csv)

            # Diccionario para almacenar las ventas por producto
            ventas_por_producto = {}

            # Procesar cada fila del archivo CSV
            for fila in lector_csv:
                producto = fila[0]
                cantidad = int(fila[1])
                precio = float(fila[2])

                # Calcular el total de ventas para el producto
                if producto in ventas_por_producto:
                    ventas_por_producto[producto] += cantidad * precio
                else:
                    ventas_por_producto[producto] = cantidad * precio

        # Identificar el producto con mayor cantidad de ventas
        producto_mayor_ventas = max(ventas_por_producto, key=ventas_por_producto.get)
        ventas_producto_mayor = ventas_por_producto[producto_mayor_ventas]

        # Identificar el producto con mayor precio promedio de venta
        producto_mayor_precio_promedio = max(ventas_por_producto, key=lambda producto: ventas_por_producto[producto] / cantidad_vendida(ventas_por_producto, producto))
        precio_promedio_producto_mayor = ventas_por_producto[producto_mayor_precio_promedio] / cantidad_vendida(ventas_por_producto, producto_mayor_precio_promedio)

        # Mostrar los resultados en la consola
        print(f"Total de ventas por producto:")
        for producto, ventas in ventas_por_producto.items():
            print(f"- {producto}: ${ventas:.2f}")

        print(f"\nProducto con mayor cantidad de ventas:")
        print(f"- {producto_mayor_ventas}: ${ventas_producto_mayor:.2f}")

        print(f"\nProducto con mayor precio promedio de venta:")
        print(f"- {producto_mayor_precio_promedio}: ${precio_promedio_producto_mayor:.2f}")
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo_csv}' no encontrado.")
    except Exception as e:
        print(f"Error al analizar el archivo de ventas: {e}")

def cantidad_vendida(ventas_por_producto, producto):
    if producto in ventas_por_producto:
        return int(ventas_por_producto[producto] / ventas_por_producto[producto][0])
    else:
        return 0

# Especificar el nombre del archivo CSV
archivo_csv = "ventas.csv"

# Ejecutar la función de análisis
#analizar_ventas(archivo_csv)



