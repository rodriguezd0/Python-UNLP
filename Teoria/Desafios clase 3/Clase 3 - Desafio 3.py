def ordenar_cadena(cadena="TEXTO"):
    cadena.split().sort(key=cadena.lower())
    return cadena
print(ordenar_cadena("holaaa tengo hambre"))
