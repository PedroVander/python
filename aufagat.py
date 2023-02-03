intentos=6

palabra="patata"
resolver=[]
letra_incorrectas=[]
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

longitud = len(palabra)
while longitud > 0:
    print("_ ", end="")
    longitud = longitud-1
letra_pedida=input("Di una letra ")

for letra in palabra:
    if letra == letra_pedida:
        print(letra, end="")
        resolver.append(letra)
    else:
        print("_ ",end="")
        letras_incorrectas.append(letra)
        