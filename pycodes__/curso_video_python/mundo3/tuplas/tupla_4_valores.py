def position (lista: list, x: int) -> int:
    indice = 0
    for i in range(len(lista)):
        if lista[i] == x:
            indice = i
            break
    return indice

import random

numeros = tuple()

for i in range(4):
    num = random.randint(1, 9)
    print('->', num)
    numeros = numeros + (num,)

print(f'A) O valor 9 apareceu {numeros.count(9)} vezes!\n')

print(f'B) O primeiro valor 3 foi digitado na posição {position(numeros, 3) + 1 if 3 in numeros else 'nenhuma'}!\n')

print(f'C) Os números pares são:\n')

for numero in numeros:
    if numero % 2 == 0:
        print(numero)