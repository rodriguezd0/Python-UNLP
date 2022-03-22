imprimir_despues = []
palabra = input('Ingresa una palabra: ')
while palabra != 'fin':
    if palabra[-1] == palabra[0]:
        imprimir_despues.append(palabra)
    palabra = input('Ingresa una palabra: ')
for i in imprimir_despues:
    print(i)
