def calcularGastos(totalViajes):

    valorActual,suma = 59,0
    while totalViajes>0:
        if totalViajes > 40:
            suma = suma+valorActual*0.6
        elif totalViajes > 30:
            suma = suma+valorActual*0.7
        elif totalViajes > 20:
            suma = suma+valorActual*0.8
        else:
            suma = suma + valorActual
        totalViajes=totalViajes-1

    return suma

cantViajes=int(input("Ingrese la cantidad de viajes: "))
Resultado=calcularGastos(cantViajes)
print(Resultado)
        

    