                                                    # execpcines

# exepciones = menejo de errores, si no hacemos nada con nuestro error se acaba nuesto codigo 
# try = corre nuesto codigo, si nuesto codigo da un error 
# except = si nuestro codigo da un error y esto nos puede hacer una excepcion que hace que se va a morir
# else = si nuesto codigo no muestra un  error se va por else 
# finally = que seria lo que se termina 

                                                    ### Exception Handling ###
numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except

try: #palabra reservada del sistema 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try: # palabra reservada del sistema
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: 
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción.
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError: # si se produce un error que no sea valueEror nuestro programa vueva a dar error
    print("Se ha producido un ValueError")
except TypeError:  # tipo derror por consola, esto se esta controlando  
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:#  manera de capturar errores
    print(error)
except Exception as my_random_error_name: # es una extencion generica 
    print(my_random_error_name)