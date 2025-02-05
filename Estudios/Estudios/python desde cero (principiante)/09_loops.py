                                                #loops 

# loops = bucles, ciclos, iteracciones, repeticiones, etc.
# while = es un bucle que se ejecuta mientras una condicion sea verdadera es como un if que se repite
# break = rompe el bucle y el significado que tiene es que se detiene la ejecucion del bucle
# for = es un bucle que se ejecuta un numero determinado a veces, y se utiliza para recorrer una secuencia de elementos
# element = elemento, es una variable que se utiliza para recorrer una secuencia de elementos
# continue = se utiliza para saltar una iteraccion en el bucle y se salta el resto del codigo en el bucle y se va a la siguiente interaccion 

my_condition = 0       # esto es una variable que tiene un valor de 0

while my_condition < 10:     #  mientras la condicion sea menor que 10 se ejecuta el bucle
    print(my_condition)      #  se imprime el mensaje y es que se ejecuta el bucle
    my_condition += 2        #  incrementa en 2 en 2 y cambia el valor de la variable
else:  # Es opcional y no se puede empezar por else.
    print("Mi condición es mayor o igual que 10") # si la condicion es mayor o igual que 10 se ejecuta un mensaje que dice que "la condicion es mayor o igual que 10 "

print("La ejecución continúa")

while my_condition < 20: # mientras la condiciones sea menos que 20 se ejecuta el bucle 
    my_condition += 1 # incrementa en 1 y cambia el valor de la variable
    if my_condition == 15: # si la condicion es igual a 15 se ejecuta el siguiente mensaje
        print("Se detiene la ejecución") # se imprime este mensaje
        break # se detiene la ejecucion del bucle, se para el bucle y no se ejecuta mas el bucle
    print(my_condition)

print("La ejecución continúa")

# For loop = bucle for, se utiliza para recorrer una secuencia de elementos 

my_list = [35, 24, 62, 52, 30, 30, 17] # lista de elementos

for element in my_list: # para cada cadena en la lista se ejecuta el bucle 
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais") # tupla de elementos

for element in my_tuple: # para cada cadena en la tupla se ejecuta el bucle
    print(element)

my_set = {"Brais", "Moure", 35} # conjunto de elementos

for element in my_set: # para cada cadena en el conjunto se ejecuta el bucle
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"} # diccionario de elementos

for element in my_dict: # para cada cadena en el diccionario se ejecuta el bucle 
    print(element)
    if element == "Edad": # si el elemento es igual a "Edad" se ejecuta el siguiente mensaje
        break # se detiene la ejecucion del bucle, se para el bucle y no se ejecuta mas el bucle
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict: 
    print(element)
    if element == "Edad": # si el elemento es igual a "Edad" se ejecuta el siguente mensaje
        continue # se salta la interaccion y se va a la siguente interaccion, y continua desde el for 
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
