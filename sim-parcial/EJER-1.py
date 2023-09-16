"""Para un programa que implementa un juego de naipes se necesita desarrollar
 la función de distribución de cartas, teniendo en cuenta lo siguiente:
   ∑En el juego pueden participar de 2 a 6 jugadores.  
   ∑Cada jugador recibe tres cartas de un mazo de baraja española,
    donde los números impresos en cada una se encuentran entre 1 y 12. 
    ∑No existen cartas repetidas y no se utilizan los 8, los 9 ni los naipes "comodines".
    ∑La función debe devolver una matriz como valor de retorno. Dicha matriz contendrá N filas
    (una por jugador) y 3 columnas (una por cada naipe), y cada elemento será una lista con un
    entero y un string (valor y "palo", por ejemplo [7, "Espadas"]).
    Desarrollar dicha función utilizando números al azar dentro de los rangos permitidos.
    Escribir también un programa para ingresar la cantidad de jugadores,
    invocar a la fun-ción pasando ese dato como parámetro e imprimir prolijamente las cartas
    que se asignaron a cada participante y que fueron devueltas por la misma. """
import random

def repartir(jugadores):
    palo=["espada","copa","oro","basto"]
    num = [1,2,3,4,5,6,7,10,11,12]
    columnas=3
    matriz=[]
    usadas=[]
    for f in range(jugadores):
        matriz.append([])
        for c in range(columnas):
            repe=False
            while repe == False:
                palo_carta=random.choice(palo)
                num_carta=random.choice(num)
                carta = str(num_carta) + palo_carta
                if carta not in (usadas):
                    matriz[f].append(carta)
                    repe=True
                    usadas.append(carta)
    return(matriz)

a=repartir(5)
print(a)



