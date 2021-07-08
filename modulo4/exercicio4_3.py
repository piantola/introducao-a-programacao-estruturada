lista = []
# Leitura da lista
for n in range(6):
    numero = input("Digite um numero " + str(n+1) + ": ")
    lista.append(numero)
# Impressao da reverso
lista.reverse()
print(lista)