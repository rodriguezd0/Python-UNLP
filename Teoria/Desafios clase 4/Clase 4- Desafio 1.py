import csv
import collections
import consolemenu
import time
from collections import Counter

def prueba():
    print(314)
    input('Enter para salir')
    return "hola"

def nueva_prueba():
    print(45555)
    input('Enter para salir')
    return "3343443"

def cargar_menu():
    catalogo,nuevo_catalogo = abrir_archivos()
    with catalogo as salida:
        with nuevo_catalogo as entrada:
            leer_catalogo = csv.reader(salida,delimiter=',')
            escribir_catalogo = csv.writer(entrada)

            menu = consolemenu.ConsoleMenu('Elegir una accion')

            funcion_1 = consolemenu.items.FunctionItem('Procesar e imprimir paises mas comunes', procesar_paises_mas_comunes,leer_catalogo)
            funcion_2 = consolemenu.items.FunctionItem('Exportar peliculas del 2021 a un archivo',procesar_anio_2021,escribir_catalogo,leer_catalogo)
            funcion_3 = consolemenu.items.FunctionItem('Leer peliculas del 2021',leer_anio_2021,leer_catalogo)

            menu.append_item(funcion_1)
            menu.append_item(funcion_2)
            menu.append_item(funcion_3)

            menu.show(show_exit_option=False)

def abrir_archivos():
    ruta = 'netflix_titles.csv'
    nuevo_archivo = 'paises del anio 2021.csv'

    catalogo = open(ruta,'r')
    nuevo_catalogo = open(nuevo_archivo,'w')

    return catalogo,nuevo_catalogo

def procesar_paises_mas_comunes(*catalogo):
    mas_comun = Counter(list(map(lambda x: x[5],catalogo))).most_common(5)
    for i in range(len(mas_comun)):
        print(f'{i+1}) {mas_comun[i][0]} con {mas_comun[i][1]} producciones')
    input('Enter para salir')

def procesar_anio_2021(escribir_catalogo,*catalogo):
    #paises_anio_2021 = list(filter(lambda x: x[7] == '2021',catalogo))
    #escribir_catalogo.writerow(next(leer_catalogo))
    #for i in paises_anio_2021:
    #    escribir_catalogo.writerow()
    #    print(i)
    #    print('='*30)
    input('Enter para salir')

def leer_anio_2021(catalogo):
    pass

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


def imprimir_mas_comunes(paises = 0):
    mas_comun = Counter(paises).most_common(5)
    for i in range(len(mas_comun)):
        print(f'{i+1}) {mas_comun[i][0]} con {mas_comun[i][1]} producciones')


if __name__ == "__main__":
    cargar_menu()

#imprimir_mas_comunes(paises)
