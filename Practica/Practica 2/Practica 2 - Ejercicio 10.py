
nombres = open('nombres_1.txt', 'r').read()
eval1 = open('eval1.txt','r').read()
eval2 = open('eval2.txt','r').read()

nombres = nombres.replace(' ','')
nombres = nombres.replace('\n','')
nombres = nombres.replace('\'','')

eval1 = eval1.replace('\n','')
eval1 = eval1.replace(' ','')

eval2 = eval2.replace('\n','')
eval2 = eval2.replace(' ','')

nombres = nombres.split(',')
eval1 = eval1.split(',')
eval2 = eval2.split(',')

def crear_tabla():
    tabla = []
    for i in range(len(nombres)):
        actual = []
        actual.append(nombres[i])
        actual.append(int(eval1[i]))
        actual.append(int(eval2[i]))
        actual.append(int(eval1[i])+int(eval2[i]))
        tabla.append(actual)
    return tabla

tabla = crear_tabla()
for i in range(len(tabla)):
    print(f'{i:>5} {tabla[i][0]:<20} {tabla[i][1]:<5} {tabla[i][2]:<5} {tabla[i][3]:<5}')
