import requests
import os
import string
import csv
import PySimpleGUI as sg
from PIL import Image, ImageTk

#4 esta el logo 7 precio 12 lenguaje
sg.theme('DarkAmber')
archivo_juegos = os.path.join(os.getcwd(),'appstore_games.csv')

layout = [[sg.Button('Close')]]

with open(archivo_juegos) as dataset:
    reader = csv.reader(dataset,delimiter=',')
    cantjuegos = 0
    for i in reader:
        if i[7] == '0' and 'es' in i[12].lower() and cantjuegos < 1:
            juego = []
            nombre = i[2]
            id = i[1]
            ruta_imagen = f'iconos/{id}.jpg'
            if not os.path.isfile(ruta_imagen):
                print(f'CREANDO {ruta_imagen}')
                icono = requests.get(i[4])
                with open(ruta_imagen,'wb') as f:
                    f.write(icono.content)
            juego.append(sg.Image(ruta_imagen,size=(10, 10)))
            juego.append(sg.Text(id))
            juego.append(sg.Text(nombre))
            layout.append(juego)
            cantjuegos+=1

window = sg.Window('Listar cosas', layout)

while True:
    event = window.read()
    if event == sg.WIN_CLOSE or event == 'Close': # if user closes window or clicks cancel
        break

window.close()
