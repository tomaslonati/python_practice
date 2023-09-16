def imiprimir_asteriscos1(filas):
    for i in range(filas):
        print("*"*10,end="")
        print()

def imprimir_asteriscos2(filas):
    for i in range(filas+1):
        cant_asteriscos=i*2
        print("*"*cant_asteriscos)


filas=int(input("Ingrese la cantidad de filas: "))

imiprimir_asteriscos1(filas)
imprimir_asteriscos2(filas)
