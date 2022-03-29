def imprimir_tipos(*args):
    for valor in args:
        print(f"{valor} es de tipo {type(valor)}")
imprimir_tipos(20,"octubre",2001,['daniel','rodriguez',188966])
