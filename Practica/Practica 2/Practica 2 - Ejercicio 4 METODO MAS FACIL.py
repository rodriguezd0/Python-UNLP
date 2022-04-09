evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

def procesar(articulo = evaluar):
    en_titulo = False
    en_resumen = False
    articulo_dividido = {'titulo':'','parrafos':''}
    complejidad_oracion = {'faciles':0,'aceptables':0,'dificiles':0,'muy dificiles':0}
    cant_oraciones = {}
    articulo = articulo.split('resumen: ')
    articulo[0] = articulo[0].replace('titulo: ','',1)
    articulo[0] = articulo[0].replace('título: ','',1)
    articulo[0] = articulo[0].replace('\n',' ')
    articulo[1] = articulo[1].replace('\n',' ')
    articulo[1] = articulo[1].split('. ')



    #Si el titulo tiene menos de 10 palabras es ok
    titulo_ok = len(articulo[0].split()) <= 10
    print('titulo esta ok' if titulo_ok else 'titulo esta MAL')

    #Cuento la cantidad de palabras parrafo por parrafo
    for i in articulo[1]:
        cant_palabras = i.split()
        cant_palabras = len(cant_palabras)
        if cant_palabras > 0:
            x = cant_palabras
            print(f'Parrafo: {i}')
            print(f'Cantidad de palabras: {x}')
            match x:
                case x if x <= 12:
                    complejidad_oracion['faciles'] += 1
                case x if x > 12 and x <= 17:
                    complejidad_oracion['aceptables'] += 1
                case x if x > 17 and x <= 25:
                    complejidad_oracion['dificiles'] += 1
                case _:
                    complejidad_oracion['muy dificiles'] += 1
            print('-'*20)

    #Imprimo la cantidad de oraciones por complejidad
    for i in complejidad_oracion:
        print(f'Oraciones {i}:{complejidad_oracion[i]}')


print("Ingrese el articulo con el siguiente formato (CTRL + D para finalizar): \n\n titulo: titulo del articulo resumen: resumen del articulo. \n")
articulo = ''

while True:
    try:
        articulo += input()
    except EOFError:
        break

if len(articulo)> 0:
    procesar(articulo)
else:
    procesar()
