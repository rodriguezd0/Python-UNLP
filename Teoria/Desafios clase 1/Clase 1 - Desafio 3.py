letra = input("Ingrese una letra: ")
if letra[0] >= 'A' and letra[0] <= 'Z':
    print("Tu letra es mayuscula")
elif letra[0]>= 'a' and letra[0] <= 'z':
    print("Tu letra es minuscula")
else:
    print("No ingresaste una letra")
