def obtenerBilletes(totalCompra, dineroRecibido):
    billetes = {
    "500": 0,
    "100": 0,
    "50": 0,
    "20": 0,
    "10": 0,
    "5":0,
    "1":0,
    }
    vuelto=dineroRecibido-totalCompra
    #error si dinero no es suficiente
    if vuelto<0:
        print("Dinero no suficienfe")
        return -1
    else:
        while vuelto > 0:
            if vuelto > 500:
                billetes["500"] += 1
                vuelto -= 500
            elif vuelto > 100:
                billetes["100"] += 1
                vuelto -= 100
            elif vuelto > 50:
                billetes["50"] += 1
                vuelto -= 50
            elif vuelto >= 20:
                billetes["20"] += 1
                vuelto -= 20
            elif vuelto >= 10:
                billetes["10"] += 1
                vuelto -= 10
            elif vuelto >= 5:
                billetes["5"] += 1
                vuelto -= 5
            elif vuelto >= 1:
                billetes["1"] += 1
                vuelto -= 1
        return billetes
vuelto = -1
#pedimos al usuario que ingrese info, si funcion devuelve error se pide nuevamente
while vuelto == -1:
    totalCompra = int(input("Ingrese el total de la compra: "))
    dineroRecibido = int(input("Ingrese el dinero recibido: "))
    vuelto = obtenerBilletes(totalCompra,dineroRecibido)


# Mostramos la cantidad de billetes a utilizar
print("El vuelto es de: ", vuelto)