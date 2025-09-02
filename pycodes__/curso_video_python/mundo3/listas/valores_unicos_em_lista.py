import random

lista_numeros = list()
print('-' * 40, end='\n')

while True:
    numero = random.randint(-1, 10)

    if numero < 0:
        print(f'Valor digitado: {numero} \nleitura finalizada.')
        break

    else:
        print(f'Valor digitado: {numero}')

        if numero in lista_numeros:
            print('Valor já digitado, não será salvo.')
        
        else:
            lista_numeros.append(numero)
            print('Valor salvo com sucesso.')

    print('-' * 40, end='\n')

print(f'Foram digitados os valores: {lista_numeros}')