class Carta:
    def __init__ (self, palo, valor): #cosntructor
        self.palo = palo
        self.valor = valor
    def __repr__ (self):
        return f"{self.valor} de {self.palo}"


carta1 = Carta("Corazones","Reina")

print(carta1)

if carta1.valor=="Reina":
    puntos=10

carta2= Carta("Tréboles", "As")

print(carta2)
valores=["As","2","3","4","5","6","7","8","9","10","Jota","Reina","Rey"]
baraja =[]
for valor in valores:
    cartanueva = Carta("picas", valor)
    cartanueva = Carta("corazones", valor)
    baraja.append(cartanueva)
print(baraja)
    