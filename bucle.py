import random

numero1 = random.randint(1, 100)
numero2=int(input("dime un numero "))
while numero1!=numero2:
    print("has fallado malisimo")
    if numero2<numero1:
        print("Es mas grande")
    else:
        print("Es mas pequeño")
    numero2=int(input("Dime un numero "))
print("¡Enhorabuena!")
    

