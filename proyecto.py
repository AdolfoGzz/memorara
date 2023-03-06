import random

#Introduccion, ingresa y regresa de nombres
def intro():
    print('--Bienvenidos a Memorama-- \n')
    print('Esto es un juego de dos, introduzcan sus nombres')
    jugador1=input('Jugador 1: ')
    jugador2=input('Jugador 2: ')
    return jugador1,jugador2

#Crea listas, una con 36 '-' y la otra con numeros 1-18 repetidos una vez y los mezcla
def creacionTableros():
    tablero=[]
    for i in range(36):
        tablero.append('-')
    tableroNum=[]
    for i in range(18):
        tableroNum.append(i+1)
        tableroNum.append(i+1)
    random.shuffle(tableroNum)
    return listaMatriz(tablero),listaMatriz(tableroNum)

#Entra una lista, y regresa una matriz de 6x6
def listaMatriz(lista):
    matriz=[]
    for i in range(6,len(lista)+1,6):
        matriz.append(lista[i-6:i])
    return matriz
    
#Imprime una matriz con el formato del tablero de juego
def imprimirTablero(tablero):
    print("    {:^3} {:^3} {:^3} {:^3} {:^3} {:^3}".format(0,1,2,3,4,5))
    print('  __________________________')
    print('  |')
    for i in range(len(tablero)):
        print(i, "|", end=' ' )
        for j in range(len(tablero[i])):
            print("{:^3}".format(tablero[i][j]), end=' ')
        print('    \n  |')
    print('\n')

#Pregunta por las cartas, checa si son iguales o no y las muestra, regresa True o False y la matriz de tablero
def preguntarCartas(tablero,tableroNum):
    while True:  #Verifica que las cordenadas escogidas no sean las mismas
        print('Escoge dos cartas diferentes con sus cordenada en el tablero')
        print('\nCarta 1')
        carta1x=int(input('X: '))
        carta1y=int(input('Y: '))
        print('\nCarta 2')
        carta2x=int(input('X: '))
        carta2y=int(input('Y: '))
        if carta1x!=carta2x or carta1y!=carta2y:
            break
    tablero[carta1y][carta1x]=tableroNum[carta1y][carta1x]  #remplaza los - por numeros en sus respectivas coordenadas
    tablero[carta2y][carta2x]=tableroNum[carta2y][carta2x]
    imprimirTablero(tablero)
    if tableroNum[carta1y][carta1x] == tableroNum[carta2y][carta2x]:
        return True,tablero
    else:
        tablero[carta1y][carta1x]='-' #vuelve a poner los - si es que o son iguales las cartas
        tablero[carta2y][carta2x]='-'
        return False,tablero
#Verifica de que jugador es el turno, y checa si el juego se ha acabdo.
def turnos(tablero,tableroNum,jugador1,jugador2):
    turno=1  #turnos pares son de jugador 2 y no pares del 1
    pares=0  #cuando se llega a 18 pares de cartas, se declara el juego como terminado
    puntos1=0 #puntos jugador 1
    puntos2=0 #puntos jugadro 2
    while True:  #Checa de quien es el turno y cuando el juego se acaba
        imprimirTablero(tablero)
        if turno%2==0: #agrega puntos al jugador correspondiente
            print('Turno de',jugador2)
        else:
            print('Turno de',jugador1)
        par,tablero=preguntarCartas(tablero,tableroNum) #regresa si las cartas son iguales y el tablero modificado si esq si eran par
        
        if par==True:
            print('\nCorrecto, vuelve a escoger\n')
            pares+=1 #agrega una par de los 18
            if turno%2==0:
                puntos2+=1
            else:
                puntos1+=1
        else:
            turno+=1 #cambia de jgador
            print('\nIncorrecto, turno del siguiente jugador\n')
        input('\nPresiona enter\n')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        if pares>=18:
            break
    if puntos1 < puntos2:
        print('Gano',jugador2,'con',puntos2,'puntos')
    elif puntos2 < puntos1:
        print('Gano',jugador1,'con',puntos1,'puntos')
    else:
        print('Es un empate!')
    print('Completaron el tablero! Felicidades')    

def main():
    jugador1,jugador2=intro()
    otroJuego=True

    #Main loop donde se verifica si los jugadores quieren seguir jugando
    while True:
        tablero,tableroNum=creacionTableros()
        while True:
            print('\nEstan list@s?')
            if (input('')) in ['si','SI','Si','Yes','yes','YES']:
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                break
            
        turnos(tablero,tableroNum,jugador1,jugador2)

        while True: #Una vez que se acaba el juego, se pregunta si se quiere volver a jugar
            print('Quieren volver a jugar?')
            otroJuego=input(''); print('\n')
            if otroJuego in ['si','SI','Si','Yes','yes','YES','no','No','NO','Sii']:
                break
        if otroJuego in ['no','No','NO']: #si es que no, se acaba, si si se repite el loop
            print('Gracias por jugar!!')
            break
    
main()