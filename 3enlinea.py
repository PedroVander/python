import random



casilla=[" "," "," "," "," "," "," "," "," "]
op=[0,1,2,3,4,5,6,7,8]
'''
|x| | |  casilla 0, 1, 2
|0| | |  casilla 3, 4, 5
|0| |x|  casilla 6, 7, 8
'''
jugar=True


while jugar:
    print("|"+casilla[0] + "|" +casilla[1]+ "|" +casilla[2]+"|")
    print("|"+casilla[3] + "|" +casilla[4]+ "|" +casilla[5]+"|")
    print("|"+casilla[6] + "|" +casilla[7]+ "|" +casilla[8]+"|")
    
    jugo=0
    
    posicion= int(input("Elige casilla del 0 al 8 "))
    casilla[posicion]="X"
    if posicion in op:
        casilla[posicion]="X"
        op.remove(posicion)
    else:
        print("Ya esta ocupado")
        posicion= int(input("Elige casilla del 0 al 8 "))
        casilla[posicion]="X"
        op.remove(pos)

    if casilla[0] == casilla[1] == casilla[2] == "X":
        print("Ganador!")
        jugar=False
        break
 
    if casilla[3] == casilla[4] == casilla[5] == "X":
        print("Ganador!")
        jugar=False
        break


    if casilla[6] == casilla[7] == casilla[8] == "X":
        print("Ganador!")
        jugar=False
        break
    

    if casilla[0] == casilla[4] == casilla[8] == "X":
        print("Ganador!")
        jugar=False
        break

    if casilla[2] == casilla[4] == casilla[6] == "X":
        print("Ganador!")
        jugar=False
        break
  
        
    if casilla[1] == casilla[4] == casilla[7] == "X":
        print("Ganador!")
        jugar=False
        break

    if casilla[0] == casilla[3] == casilla[6] == "X":
        print("Ganador!")
        jugar=False
        break
  

    if casilla[2] == casilla[5] == casilla[8] == "X":
        print("Ganador!")
        jugar=False
        break
    

    if jugo==9:
        jugar=False
        print("Empate!")
        break
        
    jugo=jugo+1
    

    ordenador=random.choice(op)
    casilla[ordenador]="O"
    op.remove(ordenador)
    if casilla[2] == casilla[5] == casilla[8] == "O":
        print("Perdedor!")
        jugar=False
        break
    if casilla[0] == casilla[3] == casilla[6] == "O":
        print("Perdedor!")
        jugar=False
        break
    if casilla[1] == casilla[4] == casilla[7] == "O":
        print("Perdedor!")
        jugar=False
        break
    if casilla[2] == casilla[4] == casilla[6] == "O":
        print("Perdedor!")
        jugar=False
        break
    if casilla[0] == casilla[4] == casilla[8] == "O":
        print("Perdedor!")
        jugar=False
        break
    if casilla[6] == casilla[7] == casilla[8] == "O":
        print("Perdedor!")
        jugar=False
        break
    if casilla[3] == casilla[4] == casilla[5] == "O":
        print("Perdedor!")
        jugar=False
        break
    if casilla[0] == casilla[1] == casilla[2] == "O":
        print("Perdedor!")
        jugar=False
        break


print("|"+casilla[0] + "|" +casilla[1]+ "|" +casilla[2]+"|")
print("|"+casilla[3] + "|" +casilla[4]+ "|" +casilla[5]+"|")
print("|"+casilla[6] + "|" +casilla[7]+ "|" +casilla[8]+"|")