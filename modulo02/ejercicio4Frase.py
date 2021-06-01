frase = input("Dime una frase: ")
letra = input("Dime una letra que quieres que te busque: ")

index = 0
contador = 0
while(index < len(frase)):
    if(frase[index].lower() == letra.lower()):
        contador += 1
    index += 1

print(f"La letra {letra} aparece {contador} veces")