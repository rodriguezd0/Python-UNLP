import string

devolver_conjunto = lambda frase_repetida: set(frase_repetida.lower())

print('Ingrese una frase')
frase = input()

#Estas lineas cuentan los espacios, si no lo hicieran tendriamos un problema
#por ejemplo, la frase 'dia ron gemus' no seria un heterograma porque tiene 2 espacios
espacios = 0
primer_espacio = True
for i in range(len(frase)):
    if frase[i] == ' ' and primer_espacio:
        primer_espacio = False
    elif frase[i] == ' ' and not primer_espacio:
        espacios +=1

print(f'{frase} es un heterograma' if (len(frase) - espacios) == len(devolver_conjunto(frase)) else f'{frase} NO es un heterograma')
