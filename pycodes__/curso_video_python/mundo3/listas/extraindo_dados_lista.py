import random

lista_numeros = list()

while True:
    numero = random.randint(-1, 10)
    print(f'Valor digitado: {numero}')

    if numero < 0:
        print('Leitura finalizada')
        print('-' * 35)
        break

    else:
        lista_numeros.append(numero)
        print('Salvo com sucesso!')

    print('-' * 35)

print(f'Você digitou {len(lista_numeros)} números, desconsiderando o -1 usado para finalizar a leitura.')

print(f'os valores em ordem decrescente são:\n{sorted(lista_numeros, reverse=True)}')

print(f'O valor 5 {'' if 5 in lista_numeros else 'não'} faz parte da lista.')