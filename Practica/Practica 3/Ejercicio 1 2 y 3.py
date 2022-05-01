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
    return len(list(filter(lambda x: pais in x[5].lower() and show == x,lista))) > 0

def determinar_si_pais_esta(cabecera,lista):
    print()
    print('Esta funcion te dice si un show tiene cierto pais. ')
    show = int(input(f'Ingresa un numero de show 1-{len(lista)}: '))
    show -= 1
    print(show)
    pais = input('Ingresa el pais: ')
    if esta_pais(lista[show],pais.lower(),lista):
        for i in range(len(lista[show])):
            print(cabecera[i]+': '+lista[show][i])
    else:
        print(f'El pais no se encuentra en el show, los paises son: {lista[show][5]}')


def informar_shows(cabecera,lista):
    anio = input('Ingrese el anio de los shows a imprimir: ')
    shows = list(filter(lambda x: anio in x[7],lista))
    for i in range(len(shows)):
        for k in range(len(shows[i])):
            print(cabecera[k], end=': ')
            print(shows[i][k])
        print('='*20)
cabecera, lista = abrir_archivo()


#Informar paises
print(lista[4])
informar_paises(lista)
input('Enter para continuar. ')
determinar_si_pais_esta(cabecera,lista)
input('Enter para continuar. ')
informar_shows(cabecera, lista)
input('Enter para salir. ')
