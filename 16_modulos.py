# Creamos un archivo llamado -> mi_modulo.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname



# Luego lo importamos desde otro archivo
## llamado main.py
## y utilizamos la función creada en el modulo llamada generate_full_name 

# main.py archivo
import mi_modulo

print(mi_modulo.generate_full_name('Apellido', 'Nombre'))
