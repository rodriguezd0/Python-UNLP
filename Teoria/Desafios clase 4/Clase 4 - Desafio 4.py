import csv
import collections
from collections import Counter

ruta = 'netflix_titles.csv'
nuevo_archivo = 'paises del anio 2021.csv'

catalogo = open(ruta,'r')
leer_catalogo = csv.reader(catalogo,delimiter=',')

nuevo_catalogo = open(nuevo_archivo,'w')
escribir_catalogo = csv.writer(nuevo_catalogo)

paises = {}

escribir_catalogo.writerow(next(leer_catalogo))

for i in leer_catalogo:
    if i[5] in paises:
        paises[i[5]]+=1
    else:
         paises[i[5]] = 1
    if i[7] == '2021':
        escribir_catalogo.writerow(i)

mas_comun = Counter(paises).most_common(5)

for i in range(len(mas_comun)):
    print(f'{i+1}) {mas_comun[i][0]} con {mas_comun[i][1]} producciones')

nuevo_catalogo.close()
