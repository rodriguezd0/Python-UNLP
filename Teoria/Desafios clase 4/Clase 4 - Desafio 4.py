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

mas_comun = Counter(paises).most_common(1)
print(f'El pais que mas produce es {mas_comun[0][0]} con {mas_comun[0][1]} producciones')
