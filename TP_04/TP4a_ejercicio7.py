def eliminar_subcadena_rebanada(cadena,posicion,caracteres):
    incicio=cadena[:posicion]
    final=cadena[posicion+caracteres:]
    nueva = incicio + final
    return nueva

def eliminar_subcadena_sin_rebanada(cadena,posicion,caracteres):
    nueva = ''
    for i in range(len(cadena)):
        if i < posicion or i >= posicion+caracteres:
            nueva+=cadena[i]
    return nueva


cadena=input("Ingrese una cadena: ")
posicion=int(input("Posición de inicio para eliminar: "))
caract=int(input("Cantidad de caracteres a eliminar: "))

solucion1=eliminar_subcadena_rebanada(cadena,posicion,caract)
print("Solución con rebanadas: ",solucion1)

solucion2=eliminar_subcadena_sin_rebanada(cadena,posicion,caract)
print("Solución sin rebanadas: ",solucion2)

