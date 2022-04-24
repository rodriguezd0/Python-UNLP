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

def determinar_si_pais_esta(cabecera,lista):
    print()
    print('Esta funcion te dice si un show tiene cierto pais. ')
    show = int(input(f'Ingresa un numero de show 0-{len(lista)-1}: '))
    pais = input('Ingresa el pais: ')
    if esta_pais(lista[show],pais.lower(),lista):
        for i in range(len(lista[show])):
            print(cabecera[i], end=': ')
            print(lista[show][i])
    else:
        print(f'El pais no se encuentra en el show, los paises son: {lista[show][5]}')



cabecera, lista = abrir_archivo()


#Informar paises
informar_paises(lista)
determinar_si_pais_esta(cabecera,lista)
