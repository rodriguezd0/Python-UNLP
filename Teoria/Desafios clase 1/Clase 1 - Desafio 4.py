caracter = input("Ingrese un caracter: ")
if caracter[0] == '\"':
    print("Tu caracter es una comilla doble")
elif caracter[0] == '\'':
    print("Tu caracter es una comilla simple")
else:
    print("No es una comilla")
