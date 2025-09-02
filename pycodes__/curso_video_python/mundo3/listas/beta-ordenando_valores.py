import random

lista_numeros = [random.randint(1, 50)]

for i in range(1, 5):
    numero = random.randint(1, 50)

    print(f'Número digitado: {numero} \n{'-' * 35}')

    for posicao, numero2 in enumerate(lista_numeros):
        if numero <= numero2:
            lista_numeros.insert(posicao, numero)
            break

        else:
            if posicao == len(lista_numeros) - 1:
                lista_numeros.append(numero)


print(f'Números digitados (em ordem crescente): {lista_numeros}')