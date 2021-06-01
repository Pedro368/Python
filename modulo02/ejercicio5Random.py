import random

numeroalearotio = random.randint(1, 20)
numerousuario = 0

while(numeroalearotio != numerousuario):
    numerousuario = int(input("Dime un numero y te dire si has acertado: "))
    if(numeroalearotio != numerousuario):
        if (numeroalearotio < numerousuario):
            print("No has acertado, es menos")
        else:
            print("No has acertado, es más")
    else:
        print("-------------------------------------------------------------------")
        print("Has acertado el número")
        print(f"numeroalearotio = {numeroalearotio}")
        print(f"numerousuario = {numerousuario}")
