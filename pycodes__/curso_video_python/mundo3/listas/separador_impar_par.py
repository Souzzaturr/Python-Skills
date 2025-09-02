import random

def eh_par (x: int) -> bool:
    return x % 2 == 0

#---------------

lista_numeros = [[],[]] #Impares(indice 0) x Pares(indice 1)

for i in range(7):
    num = random.randint(1, 9)
    print(f'Valor digitado: {num}')

    if eh_par(num):
        lista_numeros[1].insert(0, num)
    
    else:
        lista_numeros[0].insert(0, num)

    print(f'Valor {num} salvo com sucesso!!')
    print('-' * 35)

print(f'Os valores pares digitados foram: {sorted(lista_numeros[1])}\n')

print(f'Os valores impares digitados foram: {sorted(lista_numeros[0])}')