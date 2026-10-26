from funciones.menu import*
from funciones.mostrar import*
from funciones.verificarnota import*
from funciones.prome import*
from funciones.mayor import*
from funciones.impar import*
lista = []
while True:
    n = menu()
    if n == 1:
        an = int(input("ingrese la nota: "))
        v = verificarnota(an)
        if v == True:
            lista .append(an)
    elif n == 2:
        mos= mostrarlista(lista)
        print(mos)
    elif n == 3:
        res = promedio(lista)
        print(res)
    elif n == 4:
        res2 = notamacyor(lista)
        print(res2)
    elif n == 5:
        res3 = numerosimppar(lista)
        print(res3)
    else:
        break


