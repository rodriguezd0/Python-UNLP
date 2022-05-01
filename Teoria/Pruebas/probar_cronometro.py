from cronometro import cronometro
from cronometro import temporizador

cron = cronometro()
temp = temporizador()
temp.iniciar(0,0,10)
cron.iniciar()
while not temp.tiempo()[1]:
    print(temp.tiempo())
    a = input()
    if a == '1':
        print(cron.tiempo())
    elif a == '2':
        cron.pausar()
    elif a == '3':
        cron.despausar()
    elif a == '4':
        cron.detener()
