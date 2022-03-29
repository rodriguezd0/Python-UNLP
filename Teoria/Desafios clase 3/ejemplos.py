def imprimo_elementos1(uno, dos, tres, cuatro):
    """Imprimo los valores de los dos primeros parámetros"""
    print( f"{uno}, {dos}")
def imprimo_elementos2(*argumentos):
    """Imprimo los valores de los argumentos"""
    for valor in argumentos:
        print( valor)
def imprimo_elementos3(**argumentos):
    """Imprimo una tabla nombre-valor"""
    for nombre, valor in argumentos.items():
            print( f"{nombre} = {valor}")

tabla_numeros = { "uno": 1, "dos": 2, "tres":3, "cuatro": 4}
print("Invoco a imprimo_elementos3 con tabla_numeros como parámetro")
imprimo_elementos3(**tabla_numeros)
print("-" * 20)
print("Invoco a imprimo_elementos3 con los parámetros nombrados")
imprimo_elementos3(uno =1, dos = 2, tres = 3, cuatro = 4)
print("-" * 20)
print("Invoco a imprimo_elementos1 con parámetros nombrados")
imprimo_elementos1(uno ="I", dos = "II", tres = "III", cuatro = "IV")
print("-" * 20)
print("Invoco a imprimo_elementos1 con parámetros simples")
imprimo_elementos1("I", "II", "III", "IV")
print("-" * 20)
print("Invoco a imprimo_elementos2 con parámetros simples")
imprimo_elementos2(1,2,3,4)
