import random

lista_numeros = list()

for i in range(1, 6):
    numero = random.randint(1, 9)
    
    lista_numeros.append(numero)

    print(f'{i}º número: {numero}')

print('-' * 50)

maior = lista_numeros[0]
menor = lista_numeros[0]

for numero in lista_numeros[1:]:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

pos_maior = list()
pos_menor = list()

for posicao, numero in enumerate(lista_numeros):
    if numero == maior:
        pos_maior.append(posicao)
    if numero == menor:
        pos_menor.append(posicao)

print(f'O maior valor digitado foi: {maior}.')
print(f'O valor {maior} foi digitado {len(pos_maior)} vezes, nas posições:')
for posicao in pos_maior:
    print(posicao, end='...')
print()

print(f'O menor valor digitado foi: {menor}.')
print(f'O valor {menor} foi digitado {len(pos_menor)} vezes, nas posições:')
for posicao in pos_menor:
    print(posicao, end='...')