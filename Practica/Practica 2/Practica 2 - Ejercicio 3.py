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

def comparar_con_archivo(letra):
    todas_las_palabras = []
    archivo = open("textoEjercicio3.txt", "r")
    for i in archivo:
        for k in i.split():
            if k.lower().startswith(letra):
                todas_las_palabras.append(k)
    return todas_las_palabras

letra = elegir_letra()
todas_las_palabras = comparar_con_archivo(letra)

for i in todas_las_palabras:
    print(f'{i} comienza con {letra}')
