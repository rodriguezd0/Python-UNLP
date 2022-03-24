cantidad_a = 0
cadena = input("Ingrese una cadena de caracteres: ")
for i in cadena:
    if i=='a' or i=='A':
        cantidad_a+=1
print(f"La cadena contiene {cantidad_a} letras a")
