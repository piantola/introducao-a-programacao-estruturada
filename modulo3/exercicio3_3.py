def palindromo(palavra):
    palavra = palavra.upper()
    if palavra == palavra[::-1]:
        return True
    else:
        return False

print(palindromo('ovo'))
print(palindromo('teste'))
print(palindromo('palito'))
print(palindromo('arara'))