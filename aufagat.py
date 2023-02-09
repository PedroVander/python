

palabra="parisino"
resolver=[]
max_intentos=6
letra_incorrectas=[]

seguir_jugando=True

while seguir_jugando:
       
    for letra in palabra:
        if letra in resolver:
            print(letra, end="")
        else:
            print("_ ", end="")
            
    letra_pedida=input(" Di una letra ")

    if letra_pedida in palabra:
        resolver.append(letra_pedida)
    else:
        letra_incorrectas.append(letra_pedida)
        
               
    if len(letra_incorrectas)==max_intentos:
        print("Has perdido!!")
        break
    print("correctas: ", resolver)
    print("icorrectas: ", letra_incorrectas)

    if set(resolver) == set(palabra):
        seguir_jugando=False
        print("Has ganado!!")
        
        