lista = []
# Leitura da lista
for n in range(8):
    numero = input("Digite um numero " + str(n+1) + ": ")
    lista.append(numero)
# Calculo da soma dos quadrados
soma_quadrados = 0
for n in lista:
    soma_quadrados += n**2
print(soma_quadrados)