hora = input("Digite a hora: ")
if hora>=0 and hora<12:
    print("Bom dia.")
elif hora>=12 and hora<18:
    print("Boa tarde.")
elif hora>=18 and hora<=24:
    print("Boa noite.")
else:
    print("Hora invalida.")