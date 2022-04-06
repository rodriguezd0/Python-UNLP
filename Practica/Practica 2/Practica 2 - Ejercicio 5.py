import collections
frase = input('Ingrese una frase: ').lower().split()
palabras = collections.Counter(frase)
palabra_a_buscar = input('Ingrese su palabra a buscar: ').lower()
if palabra_a_buscar in palabras:
    print(f'La palabra {palabra_a_buscar} se repite {palabras[palabra_a_buscar]} veces')
