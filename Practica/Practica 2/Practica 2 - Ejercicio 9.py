filas = 4
columnas = 5

def definir_mapa(filas,columnas):
    """Esta funcion nos permite crear el mapa del buscaminas"""

    mapa = []
    print(f'El mapa actual tiene {filas} filas y {columnas} columnas, si desea cambiarlo ingrese SI')
    if input().lower() == 'si':
        print(f'Ingrese el numero de filas (Actual {filas}): ')
        filas = int(input())
        print(f'Ingrese el numero de columnas (Actual) {columnas}): ')
        columnas = int(input())
    for i in range(filas):
        fila_actual = []
        for k in range(columnas):
            columna_actual = input(f'En la fila {i+1} columna {k+1} hay bomba? (s/n): ')
            if columna_actual.lower() == 's':
                fila_actual.append('*')
            else:
                fila_actual.append(0)
        mapa.append(fila_actual)
    return filas,columnas,mapa

def calcular_mapa(filas,columnas,mapa):
    """Esta funcion recorre todo el mapa hasta encontrar una bomba,
    una vez que encuentra la bomba recorre todas las celdas que la rodean
    y les agrega un punto. Siempre cuidando de no salirnos del rango y
    de no intentar sumarle a un string"""

    for i in range(filas):
        for k in range(columnas):
            if mapa[i][k] == '*':
                #Arriba a la izquierda
                if k > 0 and i > 0:
                    if mapa[i-1][k-1] != '*':
                         mapa[i-1][k-1] +=1
                #Izquierda
                if k > 0:
                    if mapa[i][k-1] != '*':
                        mapa[i][k-1] += 1
                #Abajo a la izquierda
                if k > 0 and i < filas-1:
                    if mapa[i+1][k-1] != '*':
                        mapa[i+1][k-1] += 1
                #Arriba
                if i > 0:
                    if mapa[i-1][k] != '*':
                        mapa[i-1][k] += 1
                #Abajo
                if i < filas-1:
                    if mapa[i+1][k] != '*':
                        mapa[i+1][k] += 1
                #Arriba a la derecha
                if k < columnas-1 and i > 0:
                    if mapa[i-1][k+1] != '*':
                        mapa[i-1][k+1] += 1
                #Derecha
                if k < columnas-1:
                    if mapa[i][k+1] != '*':
                        mapa[i][k+1] += 1
                #Abajo a la derecha
                if k < columnas-1 and i < filas-1:
                    if mapa[i+1][k+1] != '*':
                        mapa[i+1][k+1] += 1
    return mapa

def imprimir_mapa(mapa):
    """Recorre el mapa y columna a columna va separando los elementos
    con un guion para luego imprimirlos en pantalla"""

    for i in mapa:
        print('')
        for k in i:
            print(k, end=' - ')

filas,columnas,mapa = definir_mapa(filas,columnas)
mapa = calcular_mapa(filas,columnas,mapa)
imprimir_mapa(mapa)
