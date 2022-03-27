
def ingresar_notas():
    alumnos = {}
    nombre = input("Ingresa un nombre: ")
    while nombre.lower() != 'fin':
        nota = input(f"Ingresa la nota de {nombre}: ")
        alumnos[nombre] = int(nota)
        nombre = input("Ingresa un nombre: ")
    return alumnos

def calcular_promedio(diccionario_alumnos):
    suma = 0
    for i in diccionario_alumnos:
        suma += diccionario_alumnos[i]
    return suma/len(diccionario_alumnos) if len(diccionario_alumnos) > 0 else 0

def imprimir_menores(diccionario_alumnos,p):
    for i in diccionario_alumnos:
        if diccionario_alumnos[i] < p:
            print(f"{i} tiene de nota {diccionario_alumnos[i]}, la cual es menor al promedio de {p}")

todos_los_alumnos = ingresar_notas()
promedio = calcular_promedio(todos_los_alumnos)

print("Lista de alumnos con nota menor al promedio: \n")
imprimir_menores(todos_los_alumnos,promedio)
