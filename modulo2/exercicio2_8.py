principal_1 = 75000
principal_2 = 215000
taxa_1 = 1.03
taxa_2 = 1.015
anos = 0
while (principal_1 < principal_2):
    principal_1 *= taxa_1
    principal_2 *= taxa_2
    anos = anos + 1
print('Jose ultrapassa Joao em ' + str(anos) + ' anos.')