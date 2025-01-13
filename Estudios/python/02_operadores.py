                                                        # operadores

# operadores aritmeticos 

print(3 + 4) # suma
print(3 - 4) # resta 
print(3 * 4) # Multiplicacion
print(3 / 4) # division 
print(3 % 4) # operacion de modulo
print(3 // 4) # flor division
print(3 ** 4) # calcular un exponente
print(2 ** 3 + 3 - 7 / 1 // 4) # todos los signos se puden hacer

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float)) # como es un valor decimal tiene que ser float y no int

# operadores comparativos 

# operaciones con enteros
print (3 > 4)  # mayor que
print (3 < 4)  # menor que 
print (3 <= 4) # menor o igual que 
print (3 >= 4) # mayor o igual que 
print (3 == 4) # operador de comparacion para igualdad
print (3 !=4)  # distintos valores 

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres cotar caracteres de una cadena de texto 
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# operadores logicos 

# Basada en el Álgebra de Boole = logica buliana rigue toda la programacion 
print(3 > 4 and "Hola" > "Python") # falso
print(3 > 4 or "Hola" > "Python") # falso
print(3 < 4 and "Hola" < "Python") # verdadero
print(3 < 4 or "Hola" > "Python") #verdadero
print(3 < 4 or ("Hola" > "Python" and 4 == 4))# verdadero        "primero hace lo del parentesis y despues sigue con lo demas"
print(not (3 > 4)) #verdadero      "para negar toda la funcion"
