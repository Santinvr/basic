                                                      #variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5 # variable entera
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # convierte el entero en un string
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False # variable booleana "verdadero o falso"
print(my_bool_variable)

#concanetaciòn de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable) # esto es una concanetacion de variable sirven para unir variables
print("Este es el valor de:", my_bool_variable)

# algunas funciones del sistema 
print(len(my_string_variable)) # cuenta los caracteres de la cadena de texto

# variables en una sola linea· ¡cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35 # esto es una forma de hacer una variable en una sola linea
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias) # esto es otra forma de hacer una variable en una sola linea 

# Inputs = pide los datos y los pone en pantalla 
name = input('¿Cuál es tu nombre? ')  # esto es para pedir datos y ponerlos en pantalla
age = input('¿Cuántos años tienes? ') # esto es para pedir datos y ponerlos en pantalla
print(name)
print(age)

# cambiamos el tipo 
name = 35 # esto es para cambiar el tipo de dato
age = "brais" 
print(name)
print (age)

# ¿Forzamos el tipo?
address: str = "Mi dirección" # esto es para forzar el tipo de dato
address = True 
address = 5
address = 1.2
print(type(address)) # sirve para ver el tipo de clase que es la variable 