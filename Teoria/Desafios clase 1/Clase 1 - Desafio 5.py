cadena_uno = input("Ingrese la cadena 1: ")
cadena_dos = input("Ingrese la cadena 2: ")
if (len(cadena_uno)>len(cadena_dos)):
    print(f"La cadena mas larga es: {cadena_uno}")
elif (len(cadena_uno)<len(cadena_dos)):
    print(f"La cadena mas larga es: {cadena_dos}")
else:
    print("Las cadenas son iguales.")
