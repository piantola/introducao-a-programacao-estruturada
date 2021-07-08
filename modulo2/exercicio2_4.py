letra = raw_input('Digite uma letra ou digito: ')
letra = letra.lower()
if letra in [0,1,2,3,4,5,6,7,8,9]:
    print('Digitou um numero.')
elif letra in ['a','e','i','o','u']:
    print('Digitou uma vogal.')
else:
    print('Digitou uma consoante.')
