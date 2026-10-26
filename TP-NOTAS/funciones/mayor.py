def notamayor(lista):
    mayor = 0
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    
    return mayor