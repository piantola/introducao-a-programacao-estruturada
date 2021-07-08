metros = input("Tamanho da area do piso: ")
caixa = (0.60*0.60*10)
total = (metros//caixa)+1
print("Comprar caixas: " + str(total))
print("Valor: " + str(total*70.00))