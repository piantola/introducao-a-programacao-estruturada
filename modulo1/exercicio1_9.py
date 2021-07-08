investimento = input("Digite o valor do investimento: ")
taxa = input("Digite taxa de juros mensal: ")
valor = investimento * (taxa/100)
print("Valor em 3 meses de investimento: " + \
    str(investimento+(valor*3)))