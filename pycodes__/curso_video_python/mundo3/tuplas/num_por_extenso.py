num = 1

while num != 0:
    numeros_extenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze')

    num = int(input('Digite um número entre 1 e 15.\n'))

    while num < 1 or num > 15:
        num = int(input('Tente novamente. Digite um número entre 1 e 15.\n'))
    
    print(f'Você digitou {numeros_extenso[num - 1]}!!')