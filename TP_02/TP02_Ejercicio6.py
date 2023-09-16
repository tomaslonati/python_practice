def normalizar(lista):
    #calcular suma de elementos
    total=sum(lista)
    for i in range(len(lista)):
        lista[i]=lista[i]/total #obtener porcentaje de cada número
    return lista

lista=[1,1,2,8,4]
lista=normalizar(lista)
print(lista)