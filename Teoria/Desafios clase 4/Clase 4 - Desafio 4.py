import csv
import collections
from collections import Counter

ruta = 'netflix_titles.csv'
catalogo = open(ruta,'r')
leer_catalogo = csv.reader(catalogo,delimiter=',')
paises = {}

for i in leer_catalogo:
    if i[5] in paises:
        paises[i[5]]+=1
    else:
         paises[i[5]] = 1

mas_comun = Counter(paises).most_common(5)

for i in range(len(mas_comun)):
    print(f'{i+1}) {mas_comun[i][0]} con {mas_comun[i][1]} producciones')
