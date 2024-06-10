def es_triangular(num):
    n = 0
    while n * (n + 1) / 2 <= num:
        if n * (n + 1) / 2 == num:
            return True
        n += 1
    return False

num = int(input("Ingrese un número: "))
if es_triangular(num):
    print(f"El número {num} es triangular.")
else:
    print(f"El número {num} no es triangular.")