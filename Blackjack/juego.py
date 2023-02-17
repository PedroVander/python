from baraja import Baraja
from mano import Mano
from bot import Manobot
mibaraja = Baraja()
manoia = Manobot()
mano1 = Mano()

mibaraja.mezclar()
# mibaraja.mostrar()
cartacogida = mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
cartacogida = mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
mano1.mostrar_mano()
mano1.calcula_valor()
vidaia=manoia.valor
print(mano1.valor)
cartacogida = mibaraja.coger_carta()
manoia.añadir_cartaia(cartacogida)
cartacogida = mibaraja.coger_carta()


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
        while True:
            manoia.calcula_valoria()
            manoia.añadir_cartaia(cartacogida)
            if manoia.valor < mano1.valor:
                cartacogida = mibaraja.coger_carta()
                manoia.añadir_cartaia(cartacogida)
            if manoia.valor == 21:
                print("Blacjack del bot")
                manoia.mostrar_manoia()
                break

            if manoia.valor > 21:
                print("Has ganado al bot")
                manoia.mostrar_manoia()
                print(manoia.valor)
                break

            if manoia.valor>mano1.valor:
                print("Ha ganado el bot")
                manoia.mostrar_manoia()
                print(manoia.valor)
                break
        

    

    
   

