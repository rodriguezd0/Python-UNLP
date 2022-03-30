import string

def elegir_letra():
    print('Ingrese una letra')
    letra = input()
    letra = letra.lower()
    if len(letra) != 1:
        print('Ingresa una unica letra.')
    elif letra not in string.ascii_letters:
        print('Por favor, ingresa una LETRA')
    else:
        return letra

letra = elegir_letra()
todas_las_palabras = input('Ingrese un texto: ')
todas_las_palabras = todas_las_palabras.split()

filtrar = list(filter(lambda x: x.lower().startswith(letra), todas_las_palabras))

for i in filtrar:
    print(f'{i} comienza con {letra}')
