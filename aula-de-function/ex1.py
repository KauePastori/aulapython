def calcula_notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6.0:
        print("Você foi aprovado!")
    else:
        print("Você foi reprovado!")

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))    

calcula_notas(nota1, nota2)