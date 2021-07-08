agulhinha = input("Preco do arroz agulhinha: ")
cateto = input("Preco do arroz cateto: ")
jasmim = input("Preco do arroz jasmim: ")
if cateto<=agulhinha and cateto<=jasmim:
    print("Comprar arroz cateto.")
elif agulhinha<=cateto and agulhinha<=jasmim:
    print("Comprar arroz agulhinha.")
else:
    print("Comprar arroz jasmim.")
