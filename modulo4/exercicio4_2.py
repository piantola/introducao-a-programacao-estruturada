lista = []
# Leitura da lista
for n in range(5):
    nota = input("Digite um numero " + str(n+1) + ": ")
    lista.append(nota)
# Impressao da media
print("Media da notas: " + str(sum(lista)/len(lista)))