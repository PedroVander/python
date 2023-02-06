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
    for letra in palabra:
     if letra == letra_pedida:
          print(letra, end="")
          resolver.append(letra)
      else:
          print("_ ",end="")
         letra_incorrectas.append(letra)
         intentos=intentos-1
        if intentos=0 
            break
        