numeros = []
def medidas():
    suma = 0
    pares = 0
    impares = 0

def preguntar_num():
        while(len(numeros) < 11):
            num = input("Dime un número: ")
            if(num.isdigit()):
                numeros.append(int(num))
                
def calcular_num(suma, numeros, numero):
    for numero in numeros:
        print(f"Número: {numero}")
        suma += numero
        if(numero % 2 == 0):
            pares += 1
        else:
            impares += 1
    return suma    
def resultados():    
    print(f"Suma Total: {suma}")
    print(f"Media: {suma / len(numeros)}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")

preguntar_num()
calcular_num()
resultados()
