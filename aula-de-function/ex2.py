def numero_de_lados(lados):
    if lados == 3:
        print("TRIÂNGULO")
    elif lados == 4:
        print("QUADRILÁTERO")
    elif lados == 5:
        print("PENTÁGONO")
    else:
        print("Valor inválido!")

numero_de_lados(7)
