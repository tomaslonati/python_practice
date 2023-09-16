"""Cuando se desea imprimir más de una copia de un trabajo que contiene varias
páginas con una aplicación como Word o Excel existe la posibilidad de intercalar
las copias o no. Por ejemplo, si el trabajo contiene tres páginas y se imprimen cuatro copias,
la secuen-cia impresa sería 1,1,1,1,2,2,2,2,3,3,3,3 sin intercalación
y 1,2,3,1,2,3,1,2,3,1,2,3 con intercalación.
Escribir un programa que permita ingresar la cantidad de páginas del trabajo y cuántas copias se desean,
 y muestre las dos secuencias que se obtendrían al imprimirlas con y sin intercalación."""

def sin_intercalar(paginas,copias):
    secuencia=[]
    for i in range(paginas):
       for j in range(copias):
           secuencia.append(i+1)
    print(secuencia)

def intercalar(paginas,copias):
    secuencia=[]
    for i in range(paginas):
       for j in range(copias-1):
           secuencia.append(j+1)
    print(secuencia)
           
sin_intercalar(3,4)
intercalar(3,4)
