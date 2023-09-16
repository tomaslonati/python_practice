#agregar entrada de socio
def registrar_ingreso(informe):
    num=int(input("Ingrese el número de socio: "))
    while num!=0:
        encontrado = False

        #si lo encuentra, se suma un ingreso
        for socio in informe:
            if num == socio[0]:
                socio[1]+=1
                encontrado = True
                break

        #si no lo encuentra, se agrega 
        if not encontrado:
            informe.append([num,1])

        num=int(input("Ingrese el número de socio: "))
    return informe

#Dar de baja a un socio
def dar_de_baja(informe):
    num=int(input("Ingrese el número de socio a dar de baja: "))
    encontrado=False
     
     #si lo encuentra, informa los ingresos eliminados y saca del informe
    for socio in informe:
            if num == socio[0]:
                print("Se han eliminado", socio[1], "ingreso(s)")
                informe.remove(socio)
                encontrado = True
    
    #si no lo encuentra encia msj de error
    if not encontrado:
         print("Número de socio no encontrado")


#PROGRAMA PRINCIPAL
informe=[]
accion=int(input("1=Registrar nuevo ingreso  /  2=Dar de baja:  "))

while accion!=-1:
    if accion==1:
        registrar_ingreso(informe)
        print(informe)

    elif accion==2:
        dar_de_baja(informe)
        print(informe)

    else:
        print("Comando no válido")
    accion=int(input("1=Registrar nuevo ingreso  /  2=Dar de baja:  "))
