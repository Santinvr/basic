                                                    #strings

my_string = "mi string"
my_other_string = 'mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" #/n esto sirve para dar un salto de linea
my_tab_string = "\tEste es un String con tabulación"         #/t esto sirve para una tabulacion en el string
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"        # esto sirve para hacer un string con espaciado y seria en una sola linea  
print(my_scape_string)

#formateo
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))# en format es para llenarlo con los parametros que teniamos ademas format va a cojer todo por eso toca ponerlo con {}
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#desempacado de caracteres
lenguaje = "python"
a, b, c, d, e, f = lenguaje
print(a)
print(e)

#division 
language_slice = lenguaje[1:3]
print(language_slice)

language_slice = lenguaje[1:]
print(language_slice)

language_slice = lenguaje[-2]
print(language_slice)

language_slice = lenguaje[0:6:2]
print(language_slice)

# al reves 
reversed_language = lenguaje[::-1]
print(reversed_language)

# Funciones del lenguaje
print(lenguaje.capitalize())#pone la primera palabra en mayuscula 
print(lenguaje.upper())#pone toda la palabra en mayusculas
print(lenguaje.count("t"))#contar cuantas letras en espesifico tiene 
print(lenguaje.isnumeric())#para saber si es un numero 
print("1".isnumeric())#para saber si es un numero 
print(lenguaje.lower())#pone toda la palabra en minusculas
print(lenguaje.lower().isupper())# para comprovar si esta en minusculas 
print(lenguaje.startswith("Py"))# para saver como va a empezar una accion 
print("Py" == "py")  # No es lo mismo