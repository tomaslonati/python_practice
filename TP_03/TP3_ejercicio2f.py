def crear_matriz(filas,columnas):
    cont=1
    matriz=[]
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            if c<=f:
                matriz[f].append(cont)
                cont+=1
            else:
                matriz[f].append(0)
        matriz[f].reverse()
    return matriz


filas=4
columnas=4
matriz=crear_matriz(filas,columnas)

for fila in matriz:
    print(fila)