                                                    #listas

my_list =list()
my_other_list = []

print(len(my_list))

my_list= [30, 62, 52, 70, 25, 18, 24]
print(my_list)
print(len(my_list))

my_other_list = [18, 1.72, "santiago", "rosero"]
print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))#cuanta los que son del mismo tipo 
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("santy"))     #donde esta el indice de santiago,en que posicion esta colocada 

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("vargas")# pone lo que queremos insertar en la lista y lo deja al final sin dañar lo que teniamos 
print(my_other_list)

my_other_list.insert(1, "Rojo")# se inserta en la posicion que queramos en la lista y lo que queremos colocar 
print(my_other_list)

my_other_list[1] = "Azul" # cambiar de lo queremos inicialmente 
print(my_other_list)

my_other_list.remove("Azul")# se elimina lo que queremos y escojemos lo que queremos 
print(my_other_list)

my_list.remove(30)# se elimina lo que queremos y escojemos lo que queremos pero si tiene 2 solo elimina 1 
print(my_list)

print(my_list.pop())# elimina el ultimo  y lo desapila 
print(my_list)

my_pop_element = my_list.pop(2)# es el elemento en el cual queremos desapilar de la lista 
print(my_pop_element)
print(my_list)

del my_list[2] #  elimina por indice,elemento en el cual no queriamos trabajar y se elimina
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()# comia lo que teniamos

my_list.clear() # vaciar los valores que teniamos 
print(my_list)
print(my_new_list)

my_new_list.reverse()# ordena los valores al reves en el mismo orden pero al reves 
print(my_new_list)

my_new_list.sort()# ordena los criterios de menor a mayor 
print(my_new_list)

# Sublistas

print(my_new_list[1:3])#es igual que los strings con las listas 

# Cambio de tipo

my_list = "Hola Python" # esto es un string y no una lista una lista tine que estar con [] para que sea una lista 
print(my_list)
print(type(my_list))    # esto es un estring a nivel de type y no se pueden hacer contantes como tal

my_list = list("hola mundo") # se pueden hacer de estas dos formas y serian una lista 
my_list = ["Hola mundo"] # se pueden hacer de estas dos formas y serian una lista 