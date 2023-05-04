def menu():
    print("Calculadora:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair do programa")

    opcao = int(input("Selecione sua opção: "))

    if opcao < 1 or opcao > 5:
        print("Opção inválida! Tente novamente.")
        return menu()

    return opcao

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Não é possível dividir por zero!"
    return x / y

while True:
    opcao = menu()

    if opcao == 5:
        print("Encerrando o programa...")
        break

    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = adicao(x, y)
        print("Resultado da adição:", resultado)

    elif opcao == 2:
        resultado = subtracao(x, y)
        print("Resultado da subtração:", resultado)

    elif opcao == 3:
        resultado = multiplicacao(x, y)
        print("Resultado da multiplicação:", resultado)

    elif opcao == 4:
        resultado = divisao(x, y)
        print("Resultado da divisão:", resultado)
