frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""

devolver_conjunto = lambda frase_repetida=frase: set(frase_repetida.lower().split())

print('Ingrese una frase (Enter para usar la frase por defecto)')
nueva_frase = input()

if nueva_frase != '':
    sin_repetir = devolver_conjunto(nueva_frase)
else:
    sin_repetir = devolver_conjunto()

for i in sin_repetir:
    print(i)
