a = input("Digite o menor numero 1: (0-1000)")
b = input("Digite o maior numero 2: (0-1000)")
if a<0 or a>1000 or b<0 or b>1000:
    print("Numeros invalidos.")
else:
    print(range(a,b+1,1))