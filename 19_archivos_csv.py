import csv

def registrar_venta():
    try:
        producto = input("Ingrese el nombre del producto: ")
        if not producto:
            raise ValueError("El nombre del producto no puede estar vacío.")

        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo.")

        precio = float(input("Ingrese el precio: "))
        if precio <= 0:
            raise ValueError("El precio debe ser un número decimal positivo.")

        with open("ventas.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([producto, cantidad, precio])
            print("Venta registrada correctamente.")
    except ValueError as e:
        print(f"Error: {e}")

while True:
    registrar_venta()
    opcion = input("¿Desea registrar otra venta? (s/n): ").lower()
    if opcion != "s":
        break
