
def ingresar_notas():
    alumnos = {}
    nombre = input("Ingresa un nombre: ")
    while nombre.lower() != 'fin':
        nota = input(f"Ingresa la nota de {nombre}: ")
        alumnos[nombre] = int(nota)
        nombre = input("Ingresa un nombre: ")
    return alumnos

def calcular_promedio(t):
    suma = 0
    for i in t:
        suma += t[i]
    return suma/len(t)

def imprimir_menores(t,p):
    for i in t:
        if t[i] < p:
            print(f"{i} tiene de nota {t[i]}, la cual es menor al promedio de {p}")

todos_los_alumnos = ingresar_notas()
promedio = calcular_promedio(todos_los_alumnos)

print("Lista de alumnos con nota menor al promedio: \n\n")
imprimir_menores(todos_los_alumnos,promedio)
