#El uso de un if else no tiene sentido, ya que un numero puede ser multiplo de varios numeros
num = input("Ingresa un numero: ")

multiplo_dos = int(num)%2 == 0
multiplo_tres = int(num)%3 == 0
multiplo_cinco = int(num)%5 == 0

if multiplo_dos:
    print("Tu numero es multiplo de 2")
if multiplo_tres:
    print("Tu numero es multiplo de 3")
if multiplo_cinco:
    print("Tu numero es multiplo de 5")
