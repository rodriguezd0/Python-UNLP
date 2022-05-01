dicci = {0:"Led Zeppelin", 2:"Deep Purple", 3:"Black Sabbath"}
y = 9
try:
    print('Vamos a entrar a otro bloque TRY')
    try:
        for x in range(1,6):
            print (dicci[z]) # OJO que estamos usando la variable z
    except KeyError:
        dicci[x] = 'Agregado'
        print('hola')
    y = y + 1
    print(f"El valor de y es {y}")
except NameError:
    print('OJO! Se está usando una variable que no existe')
    print('Se sigue con las siguientes sentencias del programa')
