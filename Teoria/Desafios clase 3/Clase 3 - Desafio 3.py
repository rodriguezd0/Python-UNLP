cadena = "hola tengo hambre"

def ordenar_cadena(cadena):
    return sorted(cadena.split(), key=str.lower)

print(ordenar_cadena(cadena))
