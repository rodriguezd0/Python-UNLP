valores = {1:'aeioulnrst',2:'dg',3:'bcmp',4:'fhvwy',5:'k',8:'jx',10:'qz'}

def conseguir_valor(letra):
    for i in valores:
        if letra in valores[i]:
            return i

def calcular_palabra(palabra):
    valor = 0
    for i in range(len(palabra)):
        valor += conseguir_valor(palabra[i])
    return valor

print('Ingrese una palabra: ')
palabra = input()
print(calcular_palabra(palabra))
