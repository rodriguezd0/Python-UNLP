def sacar_acentos(texto):
    """Saco los acentos de los nombres para poder evaluarlos mejor cuando hago la comparacion entre los dos textos"""
    sacar = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}
    for i in sacar:
        texto = texto.replace(i,sacar[i])
    return texto

def obtener_datos():
    """Obtengo los datos de los archivos y los guardo en variables, luego les borro su formato anterior y los ingreso a una lista en minusculas"""
    #Fase de lectura de archivos
    nombres_1 = open('nombres_1.txt', 'r').read()
    nombres_2 = open('nombres_2.txt', 'r').read()
    eval_1 = open('eval1.txt','r').read()
    eval_2 = open('eval2.txt','r').read()

    #Fase de modificacion de archivos
    nombres_1 = nombres_1.replace('\'','').replace('\n','').replace(' ','').lower()
    nombres_2 = nombres_2.replace('\'','').replace('\n','').replace(' ','').lower()

    nombres_1 = sacar_acentos(nombres_1)
    nombres_2 = sacar_acentos(nombres_2)

    eval_1 = eval_1.strip('\n ').split(',')
    eval_2 = eval_2.strip('\n ').split(',')

    nombres_1 = nombres_1.split(',')
    nombres_2 = nombres_2.split(',')

    return nombres_1,nombres_2,eval_1,eval_2

#Fase donde se crea la tabla
def crear_tabla(nombres_1,eval_1,eval_2):
    """"Agrego todos los elementos de nombres_1, eval_1 y eval_2 a la tabla y la devuelvo en una variable tabla"""
    tabla = []
    for i in range(len(nombres_1)):
        actual = []
        actual.append(nombres_1[i].capitalize())
        actual.append(int(eval_1[i]))
        actual.append(int(eval_2[i]))
        actual.append(int(eval_1[i])+int(eval_2[i]))
        tabla.append(actual)
    return tabla

def imprimir_datos(tabla):
    """Imprimo las listas dentro de la tabla con formato"""
    print(f'{"ID":>5} {"NOMBRE":<20} {"NOTA 1":<8} {"NOTA 2":<8} {"TOTAL":<8}')
    for i in range(len(tabla)):
        print(f'{i:>5} {tabla[i][0]:<20} {tabla[i][1]:<8} {tabla[i][2]:<8} {tabla[i][3]:<8}')

def imprimir_nombres_repetidos(nombres_1,nombres_2):
    """Hago un conjunto de la interseccion de nombres_1 y nombres_2 y los imprimo"""
    todos_los_nombres_repetidos = set(set(nombres_1) & set(nombres_2))
    for i in todos_los_nombres_repetidos:
        print(f'{i.capitalize()} esta en nombres_1 y nombres_2')
    print('='*50)

#Fase donde se imprime la tabla
nombres_1,nombres_2,eval1,eval2 = obtener_datos()
tabla = crear_tabla(nombres_1,eval1,eval2)
imprimir_nombres_repetidos(nombres_1,nombres_2)
imprimir_datos(tabla)
