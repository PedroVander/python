import random



casilla=[" "," "," "," "," "," "," "," "," "]

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
    
    jugabalidad=0 
    posicion= int(input("Elige casilla del 0 al 8 "))
    casilla[posicion]="X"

    if 
    jugabilidad=+1

    if casilla[0] == casilla[1] == casilla[2] == "X":
        print("Ganador!")
        jugar=False
        
    if casilla[0] == casilla[1] == casilla[2] == "O":
        print("Perdedor!")
        jugar=False

    if casilla[3] == casilla[4] == casilla[5] == "X":
        print("Ganador!")
        jugar=False
    if casilla[3] == casilla[4] == casilla[5] == "O":
        print("Perdedor!")
        jugar=False

    if casilla[6] == casilla[7] == casilla[8] == "X":
        print("Ganador!")
        jugar=False
    if casilla[6] == casilla[7] == casilla[8] == "O":
        print("Perdedor!")
        jugar=False

    if casilla[0] == casilla[4] == casilla[8] == "X":
        print("Ganador!")
        jugar=False
    if casilla[0] == casilla[4] == casilla[8] == "O":
        print("Perdedor!")
        jugar=False

    if casilla[2] == casilla[4] == casilla[6] == "X":
        print("Ganador!")
        jugar=False
    if casilla[2] == casilla[4] == casilla[6] == "O":
        print("Perdedor!")
        jugar=False
    if jugabilidad=9
        print("Empate!")
        jugar=False
    
   

print("|"+casilla[0] + "|" +casilla[1]+ "|" +casilla[2]+"|")
print("|"+casilla[3] + "|" +casilla[4]+ "|" +casilla[5]+"|")
print("|"+casilla[6] + "|" +casilla[7]+ "|" +casilla[8]+"|")