def peso_ideal(altura, sexo):
    if sexo == "H":
        peso_correto = (72.7 * altura) - 58
        return peso_correto
    elif sexo == "M":
        peso_correto = (62.1 * altura) - 44.7
        return peso_correto



altura = float(input("Informe a sua altura: "))
sexo = input("Informe o seu sexo (M/H): ")
a = peso_ideal(altura, sexo)
print(f"O seu peso ideal é {a}")