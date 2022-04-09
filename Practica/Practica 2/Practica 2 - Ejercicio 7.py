devolver_conjunto = lambda frase_repetida: set(frase_repetida.lower())

print('Ingrese una frase')
frase = input()

print(f'{frase} es un heterograma' if len(frase) == len(devolver_conjunto(frase)) else f'{frase} NO es un heterograma')
