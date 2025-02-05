                                                    # tuplas 

# Definición:
# una tupla no es los mismo que una lista, es muy difente porque cumple diferentes funciones 

my_tuple = tuple()
my_other_tuple = () # estas son diferentes formas de hacer una tupla 

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)
print(my_tuple)             # aqui imprime lo que seria la tupla 
print(type(my_tuple))       # esto se interpleta como una tupla por que con el type nos enseña la clase 

# Acceso a elementos y búsqueda
print(my_tuple[0])      #es dependiendo de lo que pusimos en la lista
print(my_tuple[-1])     #es dependiendo de lo que pusimos en la lista
# print(my_tuple[4]) IndexError         # esto seria un error por que no lo encontaria
# print(my_tuple[-6]) IndexError        # esto seria un error por que no lo encontaria

print(my_tuple.count("Brais"))  # Es como las listas nos cuenta lo que queremos contar 
print(my_tuple.index("Moure"))  # donde esta el indice de moure,en que posicion esta colocada 
print(my_tuple.index("Brais"))  # donde esta el indice de brais,en que posicion esta colocada 

# my_tuple[1] = 1.80 'tuple' object does not support item assignment
        # no te deja cambiar son valores constantes, no se lo puede cambiar,eliminar o modificar , no se puede hacer como tal 

# Concatenación
my_sum_tuple = my_tuple + my_other_tuple    # es el conjunto de la suma de las tuplas, no son mutables que no se puede cambiar
print(my_sum_tuple)

# Subtuplas
print(my_sum_tuple[3:6])        # buscar los elementos desde el 3 y 6

# Tupla mutable con conversión a lista
my_tuple = list(my_tuple)       
print(type(my_tuple))               # la tupla queda como clase lista por que asi la asignamos 

my_tuple[4] = "MoureDev"            # con la clase lista ya se puede cambiar 
my_tuple.insert(1, "Azul")          # una lista con nuevos valores 
my_tuple = tuple(my_tuple)          # se vueve a hacer en clase una tupla 
print(my_tuple)
print(type(my_tuple))

# Eliminación
# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion               #una tupla no se puede borrar 
del my_tuple    #
# print(my_tuple) NameError: name 'my_tuple' is not defined                             #una tupla no se puede borrar o no se puede definir 
