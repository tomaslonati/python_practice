import random

def generarlista():  #generar lista de 50 valores
    valores=[]
    for i in range(50):
        num=random.randint(1,100)
        valores.append(num)
    return valores

def repetido(lista):  #chequear si hay elementos repetidos
    vistos=[]
    flag=False
    for i in range(len(lista)):
        if lista[i] in vistos:
            flag = True
            break
        vistos.append(lista[i])
    return flag

def elementosUnicos(lista):   #cear nueva lista con los elementos únicos
    unicos=[]
    for i in range(len(lista)):
        if lista[i] not in unicos:
            unicos.append(lista[i])
    return unicos

lista=generarlista()
print(lista)

repeticion=repetido(lista)
print(repeticion)

unicos=elementosUnicos(lista)
print(unicos)





