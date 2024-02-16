"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando 
até que um valor correto seja preenchido.
"""


while True:
    nome = input("Digite seu nome completo: ")
    ano_nascimento = input(
        "Digite seu ano de nascimento (entre 1922 e 2021): ")

    try:
        nome = str(nome)
        ano_nascimento = int(ano_nascimento)

        if nome == "":
            print("o campo nome não pode ficar vazio, informar novamente")
            continue

        if ano_nascimento < 1922 or ano_nascimento > 2021:
            print("Ano de Nascimento fora do intervalo solicitado, informar novamente: ")
            continue

    except ValueError:
        print("Ano de nascimento inválido, tente novamente.")
        continue

    idade = 2022 - ano_nascimento

    print(nome, "completou ou completará ", idade, "anos em 2022")
    break
