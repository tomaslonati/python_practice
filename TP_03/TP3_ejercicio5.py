import random 

def mostrar_butacas(sala):  #imprimir filas de matriz
    cont=0
    for filas in sala:
        print("FILA",cont,filas)
        cont+=1
    print()

def cargar_sala(matriz):
    #detectar tamaño
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range (filas):   #rellenar aleatoriamente
        for c in range(columnas):
            opciones=[1,0]   #1=ocupada / 0=desocupada
            ocupacion=random.choice(opciones)
            matriz[f][c]=ocupacion
    return matriz

def reservar(sala,fila,columna):
    if sala[fila][columna]==0:  #validar ocupación
        sala[fila][columna]=1
        return True
    else:
        return False
        
def butacas_libres(sala):
    total=0
    for filas in sala:
        butacas_vacias=filas.count(0)
        total+=butacas_vacias
    return total

def butacas_contiguas(sala):  #
    mayor=0
    inicio=[0,0]
    #detectar tamaño
    filas=len(sala)
    columnas=len(sala[0])
    for f in range (filas):
        vacias=0 #reiniciar contador
        for c in range (columnas):
            if sala[f][c]==0:  #verificar si esta vacia
                vacias+=1
                if vacias>mayor:
                    mayor=vacias  #almacenar inicio 
                    inicio[0]=f
                    inicio[1]=(c+1)-vacias
            else:
                vacias=0
    return inicio


#PROGRAMA PRINCIPAL

sala = [[0,0,0,0,],
          [0,0,0,0,],
          [0,0,0,0,],
          [0,0,0,0,],
          [0,0,0,0,],
          [0,0,0,0,]]


#Mostrar y rellenar sala
mostrar_butacas(sala)

cargar_sala(sala)

mostrar_butacas(sala)

#realizar reserva
reserva=False
while reserva==False:
    fila=int(input("Ingrese la fila del asiento: "))
    colum=int(input("Ingrese la columna del asiento: "))
    reserva=reservar(sala,fila,colum)
    if reserva==True:
        print()
        print("Reserva exitosa")
        mostrar_butacas(sala)
    else:
        print("Butaca no disponible")

#mostrar cuantas quedan libres
libres=butacas_libres(sala)
print("Quedan",libres,"butacas libres")

#Ubicación butacas contiguas
conti=butacas_contiguas(sala)
print("La mayor cantida de butacas contiguas comienza en: ",conti)




