                                                            #condicionales

my_condition = True # esto es un booleano, es un tipo de dato que puede ser verdadero o falso
                    # esto es un condicional y npuede ser verdadero o falso "if"

if my_condition: # es lo mismo que decir if my_condition == true:
    print("se ejecuta la condicion del if") # si la condicion es verdadera se ejecuta este codigo

print("la ejecucion continua")

my_condition = 5 * 5    # esto es una multiplicacion, es una operacion matematica

if my_condition == 10:  # si la condicion es igual a 10 se ejecuta la condicion del if y sigue con la ejecucion
    print("Se ejecuta la condición del segundo if")

# if , elif , else

#  if = si
#  elif = sino si
#  else = sino

if my_condition > 10 and my_condition < 20: # si la condicion es mayor que 10 y menor que 20 se ejecuta la condicion de if "if se lo conoce como si funcionara"
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:    # si la condicion es igual a 25 se esecuta la condicion de elif " elif se la conoce como un sino si"
    print("Es igual a 25")
else:   # si no se cumple ninguna de las condiciones anteriores se ejecuta la condicion de else "else se lo conoce como sino", y se una ultima condicion eso significa que no cumple con ninguna de las condiciones anteriores
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Condicional con ispección de valor

my_string = ""# esto es una cadena de texto vacia lo que significa que no tiene ningun valor, es verdadero o falso  lo esta comprovando con el if 

if not my_string: # si la cadena de texto esta vacia se ejecuta la condicion del if, "not" es una negacion, lo que hace es negar la condicion.
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo": # si la cadena de texto es igual a "mi cadena de textoooooo" se ejecuta la condicion del if lo que significa que la cadena de texto es igual a "mi cadena de textoooooo" 
    print("Estas cadenas de texto coinciden")