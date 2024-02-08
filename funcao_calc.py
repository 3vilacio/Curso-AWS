# # Faça uma função calculadora de dois números com três parâmetros:
# os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada.
# Considera a seguinte definição:
# # 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calc(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2

    elif operacao == 2:
        if num1 != 0:
            return num1 - num2
        else:
            return "erro, não é possível subtrair de 0"

    elif operacao == 3:
        return num1*num2

    elif operacao == 4:
        if (num1 != 0) and (num2 != 0):
            return num1/num2
        else:
            return "erro, o não é possível dividir por 0"

    else:
        return 0


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = int(input(
    "Escolha a opção correspondente a operação desejada: (1: Soma, 2: Subtração, 3: Multiplicação e 4: Divisão): "))

resultado = calc(num1, num2, operacao)

print("Resultado: ", resultado)
