def conArchivo():
    archivo = open("textoDelReadme.txt", "r")
    for i in archivo:
        if 'http' in i.lower():
            print(i)

def conTexto():
    texto = []
    print("Ingrese el texto (CTRL + D (Linux) o CTRL + Z (Windows) para finalizar): ")
    #Leer hasta que el usuario aprete CTRL + D para finalizar la carga indicando fin de archivo
    while True:
        #En vez de EOFError podria decirle al usuario que "ingrese FIN para finalizar la carga", pero si el texto incluye una linea "FIN" no voy a poder leerlo todo correctamente
        try:
            linea = input()
        except EOFError:
            break
        #Si llega a esta linea es porque no se indico el fin de archivo y se agrega al arreglo de texto
        texto.append(linea)

    #Agregar espacios en blanco
    for i in range(10):
        print("")

    #Imprimir todas las lineas con http o https
    print("Lineas con HTTP o HTTPS")
    for i in texto:
        if 'http' in i.lower():
            print(i)

print("""Ingrese el metodo:
1 - Por archivo (textoDelReadme.txt)
2 - Por texto (Debes pegar el texto del readme)""")
eleccion = input()
if eleccion == '1':
    conArchivo()
else:
    conTexto()
