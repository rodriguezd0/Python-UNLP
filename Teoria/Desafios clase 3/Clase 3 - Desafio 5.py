import string
encriptar_letra = lambda x: chr(ord(x)+1) if x not in 'zZ' else chr(ord(x)-25)
encriptar_texto = lambda x: list(map(encriptar_letra,x))
texto_a_encriptar = input('Ingrese el texto a encriptar: ')
print(encriptar_texto(texto_a_encriptar))
