import csv
import collections
from collections import Counter


def abrir_archivos():
    ruta = 'netflix_titles.csv'
    nuevo_archivo = 'paises del anio 2021.csv'

    catalogo = open(ruta,'r')
    nuevo_catalogo = open(nuevo_archivo,'w')

    return catalogo,nuevo_catalogo


def procesar_archivo(catalogo):
    paises = {}
    with catalogo as salida:
        leer_catalogo = csv.reader(salida,delimiter=',')
        with nuevo_catalogo as entrada:
            escribir_catalogo = csv.writer(entrada)
            escribir_catalogo.writerow(next(leer_catalogo))
            for i in leer_catalogo:
                if i[5] in paises:
                    paises[i[5]]+=1
                else:
                     paises[i[5]] = 1
                if i[7] == '2021':
                    escribir_catalogo.writerow(i)
            print('Catalogo de las peliculas del anio 2021 creado correctamente.')
    return paises,escribir_catalogo


def imprimir_mas_comunes(paises):
    mas_comun = Counter(paises).most_common(5)
    for i in range(len(mas_comun)):
        print(f'{i+1}) {mas_comun[i][0]} con {mas_comun[i][1]} producciones')


catalogo,nuevo_catalogo = abrir_archivos()
paises,escribir_catalogo = procesar_archivo(catalogo)
imprimir_mas_comunes(paises)
