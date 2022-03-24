conjunto_palabras = []

for i in range(4):
    palabra = input("Ingrese una palabra: ")
    conjunto_palabras.append(palabra)

print("Listando las palabras con R: ")
for i in conjunto_palabras:
    tiene_r = False
    #Si solo una letra de la palabra tiene R, tiene_r se hace verdadero
    for k in i:
        if k=='r' or k=='R':
            tiene_r = True
    print(f"{i} TIENE R" if tiene_r else f"{i} NO TIENE R")
