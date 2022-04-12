import string
import random

# Codigo innecesario, genera usuarios aleatorios para testear
def crear_usuarios():
    lista = []
    for i in range(20):
        cantidad_iteraciones = random.randint(1,10)
        usuario = ['',0,0]
        for x in range(cantidad_iteraciones):
            usuario[0]+=(random.choice(string.ascii_letters))
        usuario[1] = random.randint(1,10)
        usuario[2] = random.randint(1,15)
        lista.append(usuario)
    return lista

def ordenar_por_nombre(lista):
    return sorted(lista, key=lambda x:x[0].lower())

mi_lista_desordenada = crear_usuarios()
mi_lista_ordenada = ordenar_por_nombre(mi_lista_desordenada)
print(mi_lista_ordenada)
