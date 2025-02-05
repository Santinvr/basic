                                                        # funciones 

# Funciones : son bloques de codigo que se pueden reutilizar en cualquier parte del programa y se pueden llamar en cualquier parte del programa 
# def = define una funcion, es una palabra clave que se utiliza para definir una funcion

def my_function(): # se define una funcion
    print("esto es una funcion") # se imprime una funcion

my_function() # se llama a la funcion
my_function()  # se llama a la funcion
my_function() # se llama a la funcion
my_function() # se llama a la funcion

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value: int, second_value): # se define una funcion con dos parametros de entrada 
    print(first_value + second_value) # se imprime la suma de los dos valores


sum_two_values(5, 7) # se llama a la funcion y se le pasan dos valores
sum_two_values(54754, 71231) # se llama a la funcion y se le pasan dos valores
sum_two_values("5", "7") #se llama a la funcion y se le pasan dos valores
sum_two_values(1.4, 5.2)# se llama a la funcion y se le pasan dos valores

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value): 
    my_sum = first_value + second_value # se define una variable que es la suma de los dos valores
    return my_sum # se retorna la variable


my_result = sum_two_values(1.4, 5.2) # se llama a la funcion y se le pasan los dos valores pueden ser decimales o enteros, pueden ser de cualquier tipo
print(my_result) # aqui no retorna nada porque la funcion no tiene return

my_result = sum_two_values_with_return(10, 5) # se llama a la funcion y se le pasan los dos valores pueden ser decimales o enteros, pueden ser de cualquier tipo
print(my_result)# aqui retorna la suma de los dos valores

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):# se define una funcion con dos parametros de entrada
    print(f"{name} {surname}") # se imprme con un formato el nombre y apellido y con un espacio entre ellos, f es para formatear


print_name(surname="Moure", name="Brais") # se le cambio el orden de valores

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"): #  se imprime alias "sin alias"
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure") # se imprime las comillas
print_name_with_default("Brais", "Moure", "MoureDev") # se imprime por defecto

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts): # para poder poner diferentes textos que queramos
    print(type(texts)) # esto seria una clase tupla 
    for text in texts: # lo hace como una lista pero insertando los valores que queramos, una funcion con parametros arbitrarios 
        print(text.upper()) # imprime todo en mayusculas los textos que queramos 


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")