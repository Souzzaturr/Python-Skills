expressao = input('Digite uma expressão matemática. ')

abre_parenteses = 0
fecha_parenteses = 0

for caractere in expressao:
    if caractere == '(':
        abre_parenteses += 1
    
    else:
        if caractere == ')':
            fecha_parenteses += 1

if abre_parenteses == fecha_parenteses:
    print('Operação está correta!!')

else:
    if abre_parenteses > fecha_parenteses:
        print('Operação incorreta.')
        print('Há parenteses abertos que não foram fechados!!')
    
    else:
        print('Operação incorreta.')
        print('Você fechou mais parenteses do que abriu!!')