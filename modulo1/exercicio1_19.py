arquivo = input("Tamanho do arquivo em MB: ")
link = input("Velocidade do link em Mbps: ")
tempo = (arquivo*8.0/link)/60.0
print("Tempo: " + str(tempo) + " minutos")