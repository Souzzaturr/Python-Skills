sexo = str(input('Digite seu sexo ("M" para Masculino, "F" para Feminino)\n')).strip().upper()

while sexo != "M" and sexo != "F":
    print('Não entendi...')
    sexo = str(input('Poderia digitar novamente seu sexo? ("M" para Masculino, "F" para feminino)\n').strip().upper())

if sexo == "M":
    print('Sexo: Masculino')

else:
    if sexo == "F":
        print('Sexo: Feminino')