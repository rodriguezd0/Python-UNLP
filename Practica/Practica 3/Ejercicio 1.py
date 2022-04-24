import csv
import os
import string

def abrir_archivo():
    carpeta = 'files'
    archivo_csv = 'netflix_titles.csv'
    ruta = os.path.join(os.getcwd(),carpeta,archivo_csv)
    archivo = open(ruta)
    lector_de_csv = csv.reader(archivo,delimiter=',')
    cabecera = next(lector_de_csv)
    lista = list(lector_de_csv)
    return cabecera, lista

def informar_paises(lista):
    retornar_paises = []
    nueva_lista = set(map(lambda x: x[5].lower(),lista))
    for i in nueva_lista:
        elementos = i.split(', ')
        for x in elementos:
            x = x.strip(',')
            retornar_paises.append(x)
    retornar_paises = sorted(set(retornar_paises))
    for i in retornar_paises:
        print(i.capitalize())

def esta_pais(show,pais,lista):
    return len(list(filter(lambda x: pais.lower() in x[5].lower() and show[3] == x[3],lista))) > 0


cabecera, lista = abrir_archivo()


#Informar paises
informar_paises(lista)
print(lista[1])
print(esta_pais(lista[1],'South Africa',lista))
