import pandas as pd

url = "https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol"
result = pd.read_html(url)

def encontrar_tabla(result):
    tabla_goleadores = -1
    for i in range(len(result)):
        if 'Goles' and 'Partidos' and 'Promedio' and 'Torneos jugados' in result[i].iloc[0]:
            tabla_goleadores = i
            break

    if tabla_goleadores == -1:
        print('No se encontro la tabla de goleadores')
        return -1
    else:
        return tabla_goleadores

id = encontrar_tabla(result)
goleadores = result[id]
goleadores = goleadores[goleadores['Goles'] > 5]
goleadores = goleadores.drop(['Pos.','Selección','Partidos','Promedio','Torneos jugados'],axis='columns')
print(goleadores)
