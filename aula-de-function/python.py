def exibir_mensagem():
    nome = input("Informe seu nome: ")
    print(f"Olá {nome}")



def par_ou_impar(numero):
    if numero % 2 == 0:
        print("par")
    else:
        print("impar")

par_ou_impar(10)