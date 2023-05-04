def  ler_numero():

    n = int(input("Informe um número inteiro: "))
    return n



def tabuada(n):
    print(f"Tabuada do {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# programa principal
numero = ler_numero()
tabuada(numero)
