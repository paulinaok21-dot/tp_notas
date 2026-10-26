def promedio(lista):
    suma = 0
    cont = 0
    promedio= 0
    for elemento in lista:
        cont = cont +1
        suma += elemento
    promedio = suma/cont
    return promedio



