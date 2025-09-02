def maior_peso (lista_composta: list) -> float:
    maior = lista_composta[0][1]
    for subitem in lista_composta:
        if subitem[1] > maior:
            maior = subitem[1]
    return maior

def menor_peso (lista_composta: list) -> float:
    menor = lista_composta[0][1]
    for subitem in lista_composta:
        if subitem[1] < menor:
            menor = subitem[1]
    return menor

#---------------

lista_pessoas = list()
pesados = list()
leves = list()
contador = 0

while True:
    nome = input('Digite um nome: ')

    if nome == '':
        print('Leitura finalizada...')
        print('-' * 35)
        break

    peso = float(input(f'Digite o peso de {nome}: '))

    dados = nome, peso
    lista_pessoas.append(dados[:])

    print(f'{lista_pessoas[contador]} adicionado com sucesso!')
    contador += 1
    print('-' * 35)

maior_pesagem = maior_peso(lista_pessoas)
menor_pesagem = menor_peso(lista_pessoas)

for pessoa in lista_pessoas:
    if pessoa[1] == maior_pesagem:
        pesados.append(pessoa)
    
    else:
        if pessoa[1] == menor_pesagem:
            leves.append(pessoa)

print(f'Ao todo, você cadastrou {len(lista_pessoas)} pessoas!\n')

print(f'O maior peso foi de {maior_pesagem}kg, pertencente à ', end = '')
for pessoa in pesados:
    print(pessoa[0], end=', ')

print('\n')
print(f'O menor peso foi de {menor_pesagem}kg, pertencente à ', end = '')
for pessoa in leves:
    print(pessoa[0], end=', ')