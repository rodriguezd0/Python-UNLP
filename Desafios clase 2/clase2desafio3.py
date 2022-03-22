lista_de_notas = []
nota = int(input("Ingresá una nota (-1 para finalizar)"))
promedio = 0
while nota != -1:
    lista_de_notas.append(nota)
    promedio+=nota
    nota = int(input("Ingresá una nota (-1 para finalizar)"))
cant=len(lista_de_notas)
if cant != 0:
    promedio/= cant
    for i in lista_de_notas:
        if i<promedio:
            print(f'LA NOTA {i} ES MENOR AL PROMEDIO {promedio}')
else:
    print('No ingresaste ningun numero')
