def numerosimppar(lista):
    listaaux=[]
    for elemento in lista:
        if elemento %2 > 0:
            listaaux.append(elemento)
        else:
            print("el numero es par")
    
    return listaaux
        

