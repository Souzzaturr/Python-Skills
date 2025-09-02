#funcoes
def eh_de_maior (x: int) -> bool:
    return 2025 - x >= 18

#codigo principal
matriz_nome_nascimento = list()

for i in range(4):
    nome = input(f'Digite o nome da {i + 1}ª pessoa.\n')
    ano_nascimento = int(input(f'Digite o ano de nascimento de {nome}.\n'))

    nome_ano = [nome, ano_nascimento]

    matriz_nome_nascimento.append(nome_ano)

for i in range(4):
    if eh_de_maior(matriz_nome_nascimento[i][1]):

        print(f'{matriz_nome_nascimento[i][0]} é de maior')
        print(f'{matriz_nome_nascimento[i][0]} tem {2025 - matriz_nome_nascimento[i][1]} anos de idade')

    else:

        print(f'{matriz_nome_nascimento[i][0]} é de menor')
        print(f'{matriz_nome_nascimento[i][0]} tem {2025 - matriz_nome_nascimento[i][1]} anos de idade')
