def menu():
    print("1. Agregar nota")
    print("2. Ver notas")
    print("3. Calcular promedio ")
    print("4. Buscar nota mayor ")
    print("5. Ver solamente notas impares") 
    print("6. Salir")
    opcion = int(input("elegi una opcion: "))
    if opcion <= 7:
            if opcion >=1:
                return opcion