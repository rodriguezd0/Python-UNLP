#Fase de lectura de archivos
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

#Fase donde se crea la tabla
def crear_tabla():
    tabla = []
    promedio = 0
    for i in range(len(nombres)):
        actual = []
        actual.append(nombres[i])
        actual.append(int(eval_1[i]))
        actual.append(int(eval_2[i]))
        actual.append(int(eval_1[i])+int(eval_2[i]))
        tabla.append(actual)
        promedio+=int(eval_1[i])+int(eval_2[i])
    promedio/=len(nombres)
    return promedio,tabla

#Fase donde se imprime la tabla
promedio,tabla = crear_tabla()
print(f'{"ID":>5} {"NOMBRE":<20} {"NOTA 1":<8} {"NOTA 2":<8} {"TOTAL":<8} PROMEDIO({promedio:<8})')
for i in range(len(tabla)):
    print(f'{i:>5} {tabla[i][0]:<20} {tabla[i][1]:<8} {tabla[i][2]:<8} {tabla[i][3]:<8}',f'{"IGUAL O POR ENCIMA DEL PROMEDIO":<8}' if tabla[i][3] >= promedio else f'{"POR DEBAJO DEL PROMEDIO":<8}')
