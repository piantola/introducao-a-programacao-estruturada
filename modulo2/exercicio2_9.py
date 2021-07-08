principal_1 = input("Informe o capital 1: ")
taxa_1 = input("Informe o taxa de juros 1: ")
principal_2 = input("Informe o capital 2: ")
taxa_2 = input("Informe o taxa de juros 2: ")
taxa_1 = taxa_1/100 + 1
taxa_2 = taxa_2/100 + 1
anos = 0
while (principal_1 < principal_2):
    principal_1 *= taxa_1
    principal_2 *= taxa_2
    anos = anos + 1
print('O primeiro ultrapassa o segundo em ' + str(anos) + ' anos.')