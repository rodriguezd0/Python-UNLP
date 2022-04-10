#Fase de lectura de archivos
def obtener_datos():
    """ Obtengo los datos de los archivos y los guardo en listas
    """
    nombres = open('nombres_1.txt', 'r').read()
    eval_1 = open('eval1.txt','r').read()
    eval_2 = open('eval2.txt','r').read()

    #Fase de modificacion de archivos
    nombres = nombres.replace('\'','').replace('\n','').replace(' ','')
    eval_1 = eval_1.strip('\n ')
    eval_2 = eval_2.strip('\n ')

    nombres = nombres.split(',')
    eval_1 = eval_1.split(',')
    eval_2 = eval_2.split(',')
    return nombres,eval_1,eval_2

#Fase donde se crea la tabla
def crear_tabla(nombres,eval_1,eval_2):
    """Ingreso todos los datos a una matriz y mientras los ingreso calculo el promedio"""
    tabla = []
    promedio = 0
    for i in range(len(nombres)):
        actual = []
        actual.append(nombres[i])
        actual.append(int(eval_1[i])+int(eval_2[i]))
        tabla.append(actual)
        promedio+=int(eval_1[i])+int(eval_2[i])
    promedio/=len(nombres)
    return promedio,tabla

def imprimir_datos(promedio,tabla):
    """Recorro toda la tabla"""
    print(f'{"ID":>5} {"NOMBRE":<20} {"TOTAL":<8} PROMEDIO({promedio:<8})')
    for i in range(len(tabla)):
        print(f'{i:>5} {tabla[i][0]:<20} {tabla[i][1]:<8}',f'{"IGUAL O POR ENCIMA DEL PROMEDIO":<8}' if tabla[i][1] >= promedio else f'{"POR DEBAJO DEL PROMEDIO":<8}')


nombres,eval1,eval2 = obtener_datos()
promedio,tabla = crear_tabla(nombres,eval1,eval2)
imprimir_datos(promedio,tabla)
