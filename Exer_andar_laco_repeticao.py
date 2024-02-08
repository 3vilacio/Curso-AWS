# Imprimir um numero para cada andar de um hotel de 20 andares com exceção do 13

# usando o FOR
print("------------------------------------------")
print("Questão:1")
print()
for i in range(1, 21):  # números dos andares
    if i != 13:  # verificação da condição pedida, caso o i seja diferente de 13 ele vai printar na tela.
        print(i)  # exibição do resultado
print("------------------------------------------")

# usando o WHILE e a exibição em ordem descrecente
print("------------------------------------------")
print()
print("Questão: 2")
print()
i = 20

while i >= 1:
    if i != 13:
        print(i)
    i = i-1
print("------------------------------------------")
