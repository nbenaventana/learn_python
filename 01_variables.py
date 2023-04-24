# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)

# Variables de distintos tipos

first_name = 'Nelson'
last_name = 'Benaventana'
country = 'Argentina'
city = 'Concordia'
age = 44
is_married = True
skills = ['HTML', 'CSS', 'Java Script', 'React', 'Python']
person_info = {
    'firstname':'Nelson', 
    'lastname':'Benaventana', 
    'country':'Argentina',
    'city':'Concordia'
    }
print("Valor de tipo Dictionary: " + person_info['firstname'])

print("Tipo Set variable Skills subindice 2: " + skills[2])


# Mostramos los valores de las variables

print('Primer nombre:', first_name)
print('Cantidad de caracteres del primer Nombre:', len(first_name))
print('Apellido: ', last_name)
print('Cantidad de caracteres del Apellido: ', len(last_name))
print('Pais: ', country)
print('Ciudad: ', city)
print('Edad: ', age)
print('Casado: ', is_married)
print('Habilidades: ', skills)
print('Información personal: ', person_info)
