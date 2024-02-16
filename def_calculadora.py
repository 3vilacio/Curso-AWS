"""

Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

"""


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if a == 0:
        return "Erro: Divisão por zero"

    elif b == 0:
        return "Erro: Divisão por zero"

    else:
        return a / b


def calculadora():
    while True:
        print("\n1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input(
            "Informar o número correspondente a operação desejada: ")

        if escolha == "0":
            print("A opção sair foi selecionada.")
            break
        elif escolha in {"1", "2", "3", "4"}:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                resultado = soma(num1, num2)
                print("Resultado:", resultado)
            elif escolha == "2":
                resultado = subtracao(num1, num2)
                print("Resultado:", resultado)
            elif escolha == "3":
                resultado = multiplicacao(num1, num2)
                print("Resultado:", resultado)
            elif escolha == "4":
                resultado = divisao(num1, num2)
                print("Resultado:", resultado)
        else:
            print("Essa opção não existe, informar uma opção válida: ")


calculadora()
