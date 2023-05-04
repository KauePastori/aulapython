def true_or_false(inteiro):
    if inteiro % 2 == 0:
        return True
    else:
        return False


inteiro = int(input("Informe o numero: "))
valor = true_or_false(inteiro)
print(valor)
