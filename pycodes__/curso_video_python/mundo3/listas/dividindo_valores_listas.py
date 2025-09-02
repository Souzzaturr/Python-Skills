import random

lista_numeros = list()
lista_impares = list()
lista_pares = list()
numero = 0

while True:
    numero = random.randint(-1, 20)
    print(f'Valor digitado: {numero}')

    if numero < 0:
        print(f'Leitura finalizada.')
        print('-' * 35)
        break

    else:
        lista_numeros.append(numero)
        if numero % 2 == 0:
            lista_pares.append(numero)
        
        else:
            lista_impares.append(numero)
        
        print('Salvo com sucesso!')
        print('-' * 35)

print(f'A lista de todos os números válidos (maiores ou iguais a zero) é: \n{lista_numeros}\n')

print(f'Dos números digitados, os números PARES são: \n{lista_pares}\n')

print(f'Dos números digitados, os números IMPARES são: \n{lista_impares}\n')