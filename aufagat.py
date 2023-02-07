intentos=6

palabra="patata"
resolver=[]

letra_incorrectas=[]

longitud = len(palabra)
while longitud > 0:
    print("_ ", end="")
    longitud = longitud-1
while True:
    letra_pedida=input("Di una letra ")
    if letra == letra_pedida:
        resolver.append(resolver)
        print(resolver)
    else:
        letra_incorrectas.append(letra_incorrectas)
        print(letra_incorrectas)
    for letra in palabra:
        if letra in resolver:
            print(letra, end="")
        else:
            print("_ ", end="")
    
        
        