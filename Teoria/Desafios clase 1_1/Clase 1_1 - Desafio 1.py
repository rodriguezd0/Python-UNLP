palabras_con_r = []
for i in range(4):
    palabra = input("Ingrese una palabra: ")
    tiene_r = False
    for k in palabra:
        if k=='r' or k=='R':
            tiene_r = True
    if tiene_r:
        palabras_con_r.append(palabra)

print("Listando las palabras con R: ")
for i in palabras_con_r:
    print(i)