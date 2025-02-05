                                                    #clases
# clases = poder identificar nuestra clase o nuestro codigo el cual vamos a ejecutar
class MyEmptyPerson: # esto es suficiente para nombrar la clase 
    pass  # Para poder dejar la clase vacía, algo que no pueda hacer nada


print(MyEmptyPerson)#podemos poner una clase con () o sin, pero igualmente nos va a cojer
print(MyEmptyPerson())#podemos poner una clase con () o sin, pero igualmente nos va a cojer

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"): #constuctor de clase "int,self"
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública = se le puede pasar lo que sea, es un constructor
        self.__name = name  # Propiedad privada

    def get_name(self): # retorna a la persona del nombre 
        return self.__name

    def walk(self):# WALK es caminar
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev") 
print(my_other_person.full_name) # se coloca en el orden en el que esta y alias estaria en()
my_other_person.walk() 
my_other_person.full_name = "Héctor de León (El loco de los perros)" # se cambia el nombre
print(my_other_person.full_name)

my_other_person.full_name = 666 # se cambia lo que queremos  
print(my_other_person.full_name)