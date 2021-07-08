lista = list()
for i in range(6):
    lista.append(input("Digite o numero " + str(i+1) + ": "))
print(sum(lista))
print(sum(lista)/len(lista))