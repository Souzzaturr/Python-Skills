import random

def eh_par (x: int) -> bool:
    return x % 2 == 0

def maior (lista: list) -> int:
    maior = lista[0]
    for elemento in lista[1:]:
        if elemento > maior:
            maior = elemento
    return maior

matriz = list()

for i in range(1, 4):
    print(f'Linha {i}')
    linha = list()
    
    for j in range(3):
        celula = random.randint(1, 999)
        print(f'Número digitado: {celula}')

        linha.append(celula)

        print(f'Número {celula} salvo com sucesso!!\n')
    
    matriz.append(linha[:])
    print('-' * 35)

print(f'MATRIZ DEFINIDA COM SUCESSO!!\n')

for linha in matriz:
    for celula in linha:
        print(f'[{celula:0>3}]', end='')

    print()
print('\n', '-' * 35)

soma_elementos_pares = 0

for linha in matriz:
    for celula in linha:
        if eh_par(celula):
            soma_elementos_pares += celula

print(f'A soma de todos os valores pares é: {soma_elementos_pares}\n')

soma_terceira_coluna = 0

for linha in matriz:
    soma_terceira_coluna += linha[2]

print(f'A soma de todos os elementos da tercera coluna é: {soma_terceira_coluna}\n')

print(f'O maior elemento da 2ª linha dessa matriz é: {maior(matriz[1])}')