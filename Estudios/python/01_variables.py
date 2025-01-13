                                                      #variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#concanetaciòn de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# algunas funciones del sistema 
print(len(my_string_variable))

# variables en una sola linea· ¡cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs = pide los datos y los pone en pantalla 
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# cambiamos el tipo 
name = 35
age = "brais"
print(name)
print (age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))