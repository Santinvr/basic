                                                    #diccionarios 

my_dicts = dict()   # esta es una forma de hacer un diccionario
my_other_dicts = {} # esta es otra forma de hacer un diccionario

print(type(my_dicts))        # nos esta diciendo que es una clase diccionario
print( type(my_other_dicts)) # nos esta diciendo que es una clase diccionario, pero esta vacio

my_other_dicts = {"nombre": "santiago", "apellido": "ordoñez", "edad": 18, 1:"python"} # es un lenjuaje es fuertemente no etipado y se debe definir el tipo de datos o de clase que se va a utilizar 

my_other_dicts = {"nombre": "santiago",
                  "apellido": "ordoñez", "edad": 18, 1: "python"} # se puede tener diferentes tipos de dados en un diccionario

# esta es otra forma de hacer un diccionario
my_dicts = { 
    "nombre": "santiago",
    "apellido": "ordoñez",
    "edad":18,
    "lenguajes": {"python", "java", "c++"}, # almacenar datos de tipo valor en un diccionario
    1:1.74
    } 
# se puede poner diferentes tipo de datos dentro de un diccionario

print(my_other_dicts)
print(my_dicts)

print(len(my_other_dicts))      # nos esta diciendo cuantos elementos tiene el diccionario
print(len(my_dicts))            # en realidad nos esta diciendo cuantos elementos tiene el diccionario

# Búsqueda

print(my_dicts[1])              # aqui nos esta diciendo que elk valor de la clave 1 es 1.74
print(my_dicts["nombre"])       # nos esta diciendo que el valor de la clave nombre es santiago

print("ordoñez" in my_dicts)    # nos esta diciendo que si el apellido esta en el diccionario, nos va a decir si es verdadero o falso 
print("apellido" in my_dicts)   # nos esta diciendo que si el apellido esta en el diccionario, por que esta en las claves y no en los valores

# Inserción

my_dicts["Calle"] = "Calle MoureDev" # aqui nos esta diciendo que la clave calle tiene el valor de calle mouredev
print(my_dicts)

# Actualización

my_dicts["mombre"] = "Pedro"        # aqui no esta diciendo que el nuevo valor actualizado de la clave nombre es pedro
print(my_dicts["nombre"]) 

# Eliminación

del my_dicts["Calle"]               # aqui nos esta diciendo que se elimino la clave calle de nuestro diccionario
print(my_dicts)

# Otras operaciones

print(my_dicts.items()) # es un listado con cada uno de los elementos del diccionario
print(my_dicts.keys())  # es un listado con cada una de las claves del diccionario ["nombre","apellido","edad","lenjuajes",1]
print(my_dicts.values()) # es un listado con cada una de las claves del diccionario ["santiago","ordoñez",18,{"python","java","c++"},1.74]

my_list = ["Nombre", 1, "Piso"]# es una lista con diferentes tipos de datos 

my_new_dict = dict.fromkeys((my_list))# es una forma de crear un diccionario a partir de una lista 
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # es una forma de crear un diccionario a partir de una lista 
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dicts)# es una forma de crear un diccionario, es algo muy rebuscado, es un diccionario vacio
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dicts, "MoureDev") # es un valor que se va a duplicar en cada una de las claves
print((my_new_dict))

my_values = my_new_dict.values()# es una forma de obtener los valores de un diccionario,y es una clase de tipo de dato "dict_values"
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))# es una forma de obtener los valores de un diccionario, y convertirlo en una lista y luego en un diccionario
print(tuple(my_new_dict))
print(set(my_new_dict))