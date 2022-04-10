#Fase de lectura de archivos
todo_a_minuscula = lambda x: x.lower()
nombres_1 = open('nombres_1.txt', 'r').read()
nombres_2 = open('nombres_2.txt', 'r').read()
eval_1 = open('eval1.txt','r').read()
eval_2 = open('eval2.txt','r').read()

#Fase de modificacion de archivos
nombres_1 = nombres_1.replace('\'','').replace('\n','').replace(' ','')
nombres_2 = nombres_2.replace('\'','').replace('\n','').replace(' ','')
eval_1 = eval_1.strip('\n ')
eval_2 = eval_2.strip('\n ')

nombres_1 = nombres_1.split(',')
nombres_2 = nombres_2.split(',')
eval_1 = eval_1.split(',')
eval_2 = eval_2.split(',')

nombres_1 = list(map(todo_a_minuscula,nombres_1))
nombres_2 = list(map(todo_a_minuscula,nombres_2))

#Fase donde se crea la tabla
def crear_tabla():
    tabla = []
    for i in range(len(nombres_1)):
        actual = []
        actual.append(nombres_1[i].capitalize())
        actual.append(int(eval_1[i]))
        actual.append(int(eval_2[i]))
        actual.append(int(eval_1[i])+int(eval_2[i]))
        tabla.append(actual)
    return tabla

#Indicar los nombres repetidos
todos_los_nombres_repetidos = set(set(nombres_1) & set(nombres_2))
for i in todos_los_nombres_repetidos:
    print(f'{i.capitalize()} esta en nombres_1 y nombres_2')
print('='*50)

#Fase donde se imprime la tabla
tabla = crear_tabla()
print(f'{"ID":>5} {"NOMBRE":<20} {"NOTA 1":<8} {"NOTA 2":<8} {"TOTAL":<8}')
for i in range(len(tabla)):
    print(f'{i:>5} {tabla[i][0]:<20} {tabla[i][1]:<8} {tabla[i][2]:<8} {tabla[i][3]:<8}')
