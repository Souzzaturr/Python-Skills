import random

lista_3_numeros = tuple()

for i in range(3):
    lista_3_numeros = lista_3_numeros + (random.randint(1, 9),)

print('Listagem de números gerados:\n')

for numero in lista_3_numeros:
    print(numero)


print('-' * 45)

print(f'O menor valor é {min(lista_3_numeros)}')


print('-' * 45)

print(f'O maior valor é {max(lista_3_numeros)}')