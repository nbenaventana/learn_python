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

first_name = 'Nelson'    #cadena de caracteres
last_name = 'Benaventana' #cadena de caracteres
country = 'Argentina' #cadena de caracteres
city = 'Concordia' #cadena de caracteres
age = 44 #entero
is_married = True  #booleano> verdadero o falso
skills = ['HTML', 'CSS', 'Java Script', 'React', 'Python'] #lista de cadenas
person_info = {
    'firstname':'Nelson', 
    'lastname':'Benaventana', 
    'country':'Argentina',
    'city':'Concordia'
    }   #Esto es un diccionario de datos, clave : valor

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
