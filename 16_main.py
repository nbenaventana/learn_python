# main.py archivo
#De esta forma se importa el modulo para utilizar sus 
#funciones y variables
import mi_modulo

print(mi_modulo.generate_full_name('Apellido', 'Nombre'))

# Importar funciones desde un modulo
## Podemos tener muchas funciones en un archivo y podemos importar todas las funciones de manera diferente.

from mi_modulo import generate_full_name, sum_dos_nums, persona, gravedad, pi

print(generate_full_name('Alberto','Perez'))

print(sum_dos_nums(1,9))

mass = 100

peso = mass * gravedad

print(peso)

print(persona['nombre'])

