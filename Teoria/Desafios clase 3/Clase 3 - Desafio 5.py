import string
encriptar_letra = lambda x: chr(ord(x)+1) if x not in 'zZ' else chr(ord(x)-25)
encriptar_texto = lambda x: list(map(encriptar_letra,x))
unir_texto = lambda x: ''.join(x)
texto_a_encriptar = input('Ingrese el texto a encriptar: ')
texto_a_encriptar = encriptar_texto(texto_a_encriptar)
print(unir_texto(texto_a_encriptar))
