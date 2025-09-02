print('Escolha um numero decimal inteiro qualquer, e eu (programa) irei converte-lo para uma de três bases.')

numero = int(input('Digite abaixo o número: \n'))
print(f'Número inteiro decimal escolhido = {numero}')

print('Bases disponíveis para conversão:')
print('Binário -> 1')
print('Octal -> 2')
print('Hexadecimal -> 3')

escolha = int(input('Digite um dos três numeros (1, 2, 3) para escolher uma conversão a ser realizada. \n'))

if escolha == 1:
    print('Conversão escolhida: Decimal -> Binário')
    print(f'Número decimal {numero} em binário = {bin(numero)}')

else:
    if escolha == 2:
        print('Conversão escolhida: Decimal -> Octal')
        print(f'Número decimal {numero} em octal = {oct(numero)}')

    else:
        if escolha == 3:
            print('Conversão escolhida: Decimal -> Hexadecimal')
            print('Número decimal {numero} em Hexadecimal = {hex(numero)}')

        else:
             print('Cógido não entendido :/')
