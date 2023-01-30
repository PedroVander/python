import random

while True:
    eleccion=["papel","tijera","piedra"]
    pc = random.choice(eleccion) 
    eleccion=input("Piedra,papel y tijera saca lo que nunca quieras 1, 3, 2 ya! ")
    
    if eleccion==pc:
        print("Empate")
    if eleccion=="piedra" and pc=="tijera":
        print("El robot ha sacado tijera")
        print("Ganaste!")
    if eleccion=="piedra" and pc=="papel":
        print("El robot ha sacado papel")
        print("Perdiste! Que malo")
    if eleccion=="papel" and pc=="tijera":
        print("El robot ha sacado tijera")
        print("Perdiste! Que malo")
    if eleccion=="papel" and pc=="piedra":
        print("El robot ha sacado piedra")
        print("Ganaste!")
    if eleccion=="tijera" and pc=="papel":
        print("El robot ha sacado papel")
        print("Ganaste!")
    if eleccion=="tijera" and pc=="piedra":
        print("El robot ha sacado piedra ")
        print("Perdiste! Que malo")