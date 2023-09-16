def extraer_subcadena_reb(cadena,posicion,cantidad):
    subcad=cadena[posicion:posicion+cantidad]
    return subcad

def extraer_subcadena_sin_reb(cadena,posicion,cantidad):
    subcadena=""
    for i in range(len(cadena)):
        if i>=posicion and i<posicion+cantidad:
            subcadena+=cadena[i]
    return subcadena

cad=input("Ingrese una cadena: ")
pos=int(input("Ingrese la posicion inicial de la subcadena: "))
cant=int(input("Ingrese la cantidad de caracteres a extraer: "))

sol_reb=extraer_subcadena_reb(cad,pos,cant)
print("Solución con rebanadas: ",sol_reb)

sol_sin_reb=extraer_subcadena_sin_reb(cad,pos,cant)
print("Solución sin rebanadas: ",sol_sin_reb)

