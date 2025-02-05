                                                        #sets

my_set = set()      # esta es una forma de hacer un set 
my_other_set = {}   # esta es otra forma de hacer un set pero no es un set, es un diccionario

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))   # esto es un set, ya no es un diccionario "un diccionario es cuando esta vacio {}"
print(len(my_other_set))    # muesta los elementos que tiene un set 

# Inserción

my_other_set.add("MoureDev") # esto añade un elemento al set 
print(my_other_set)          # Un set no es una estructura ordenada, por lo que no se garantiza el orden de inserción
my_other_set.add("MoureDev") # Un set no admite repetidos, en lo cual no se va a añadir y se ordena todo el set
print(my_other_set)          # no nos asegura el orden de insercion

# Búsqueda

print("Moure" in my_other_set) # esto dice si esta o no esta en un set 
print("Mouri" in my_other_set) # nos dice dice si esta o no esta en un set, mediante un booleano "true o false"

# Eliminación

my_other_set.remove("Moure") # esto eliminaria un elemento del set, si no lo encuentra nos da un error, y no se puede eliminar un elemento que no esta 
print(my_other_set)

my_other_set.clear()        # esto eliminaria todos los elementos del set, esto lo deja vacio y no se puede recuperar 
print(len(my_other_set))

del my_other_set            # esto elimina el set por completo con la palabra reservada del
# print(my_other_set) NameError: name 'my_other_set' is not defined # esto nos dice que no esta definido por que ya lo eliminamos o no existe como tal 

# Transformación

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)                           # esto se convierte en una lista el set que teniamos 
print(my_list)
print(my_list[0])                                # esto es muy ariesgado por que no se sabe que elemento se va a imprimir, por que no se sabe el orden de insersion

my_other_set = {"Kotlin", "Swift", "Python"}     # es otro set y se puede hacer una lista, se puede hacer una lista de un set

# Otras operaciones

my_new_set = my_set.union(my_other_set)                                       # esto une los dos sets y no se repiten los elementos, se ordenan de manera aleatoria
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # esto une los sets y no se repiten los elementos, se ordenan de manera aleatoria
print(my_new_set.difference(my_set))                                          # esto nos da la diferencia de los sets y nos da los elementos que no se repiten 