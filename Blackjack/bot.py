
class Manobot:
    def __init__(self):
        self.cartas = []
        self.valor = 0
        
        
    def añadir_cartaia(self, carta):
            self.cartas.append(carta)
    def mostrar_manoia(self):
        for carta in self.cartas:
            print(carta)
    def calcula_valoria(self): 
        self.valor=0
        for carta in self.cartas:
            if carta.valor in ["Reina", "Rey", "Jota", "10" ]:
                self.valor +=10
            elif carta.valor == "As":
                self.valor +=11
            else:
                self.valor += int(carta.valor) # 1 <-"1"