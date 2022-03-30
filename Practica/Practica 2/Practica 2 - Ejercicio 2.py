from collections import Counter
todas_las_palabras = []
with open("textoDelReadme.txt", 'r') as archivo:
    for i in archivo:
        for k in i.split():
            todas_las_palabras.append(k)

def con_for():
    cantidad_palabras = {}

    #Proceso las cantidades
    for i in todas_las_palabras:
        if i.lower() in cantidad_palabras:
            cantidad_palabras[i.lower()] += 1
        else:
            cantidad_palabras[i.lower()] = 1

    maximo = max(cantidad_palabras, key= lambda x: cantidad_palabras[x])
    print(f"La palabra que mas se repite es \"{maximo}\" con {cantidad_palabras[maximo]} repeticiones.")

def con_counter():
    c = Counter(todas_las_palabras)
    mas_comun = c.most_common(1)[0]
    print(f"La palabra mas comun es \"{mas_comun[0]}\" con {mas_comun[1]} repeticiones.")

eleccion = input("Ingrese a(for) b(counter): ")
if eleccion=='a':
    con_for()
else:
    con_counter()
