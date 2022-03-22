lista_de_notas = []
nota = int(input("Ingresá una nota (-1 para finalizar)"))
promedio = 0
cantidad = 0
while nota != -1:
    lista_de_notas.append(nota)
    cantidad+=1
    promedio+=nota
    nota = int(input("Ingresá una nota (-1 para finalizar)"))
promedio/=cantidad
for i in lista_de_notas:
    if i<promedio:
        print(f'LA NOTA {i} ES MENOR AL PROMEDIO {promedio}')
