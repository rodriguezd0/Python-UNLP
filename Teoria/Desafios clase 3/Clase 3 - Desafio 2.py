def imprimo_muchos_valores(mensaje_inicial, *en_otro_idioma, **en_detalle):
    print("Mensaje original")
    print(mensaje_inicial)
    print("\nEn otros idiomas")
    print("-" * 40)
    #Imprimo todos los valores que se encuentran en la tupla en_otro_idioma
    for val in en_otro_idioma:
        print(val)
    print("\nEn detalle")
    print("-" * 40)
    #Imprimo los valores del diccionario
    #Tambien podria hacer asi:
    #for clave, valor in en_detalle.items():
    #   print(f"{clave}: {valor}")
    for clave in en_detalle:
        print(f"{clave}: {en_detalle[clave]}")
    print("\nFuente: traductor de Google. ")

#El primer valor "Hola", se guarda en la variable mensaje_inicial

#Los valores "hello", "Hallo", "Aloha", "Witam" , "Kia ora" ingresan a la tupla en_otro_idioma

#Los valores ingles,aleman,hawaiano,polaco y maori ingresan a un diccionario con sus respectivos valores

imprimo_muchos_valores("Hola",
    "hello", "Hallo", "Aloha ", "Witam", "Kia ora",
    ingles= "hello",
    aleman="Hallo",
    hawaiano="Aloha",
    polaco="Witam",
    maori="Kia ora")
