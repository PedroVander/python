from baraja import Baraja
from mano import Mano

mibaraja = Baraja()

mano1 = Mano()

mibaraja.mezclar()
# mibaraja.mostrar()
cartacogida = mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
cartacogida = mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
mano1.mostrar_mano()
mano1.calcula_valor()
print(mano1.valor)

while True:
    estado=mano1.valor
    if estado ==21:
        print("BlackoJacko, has ganado")
        break
    if estado > 21:
        print("Has perdido que malo")
        break
    pedir_carta = input("Quieres otra carta ? s/n ")
    if pedir_carta == "s":
        cartacogida = mibaraja.coger_carta()
        mano1.añadir_carta(cartacogida)
        mano1.mostrar_mano()
        mano1.calcula_valor()
        print(mano1.valor)
    else:
        break
        print("Gracias por jugar")
    

    
   

