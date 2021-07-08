nome = raw_input('Nome: ')
if len(nome)<3:
    print('Nome menor que 3 caracteres.')
idade = input('Idade: ')
if idade<0 or idade>130:
    print('Idade invalida.')
salario = input('Salario: ')
if salario<0:
    print('Salario invalida.')
cep = raw_input('CEP: ')
if len(cep)!=8:
    print('CEP invalida.')
dep = raw_input('Departamento: ')
if dep!='Administrativo' and dep!='Fabrica':
    print('Departamento invalida.')