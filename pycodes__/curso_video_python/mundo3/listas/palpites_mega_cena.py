import random

while True:
    print('-' * 50)
    print(f'{'JOGO DA MEGA SENA': ^50}')
    print('-' * 50, '\n')

    qtd_jogos = int(input('Digite quantos jogos você quer que eu sorteie pra você.\n'))

    if qtd_jogos < 1:
        print('FINALIZANDO PROGRAMA...')
        break

    print(f'{f' SORTEANDO {qtd_jogos} JOGOS ':=^50}', end='\n\n')

    for i in range(1, qtd_jogos + 1):
        jogo = list()

        for j in range(6):
            num_da_sorte = random.randint(1, 60)

            jogo.append(num_da_sorte)
        
        print(f'{f'Jogo {i}: {jogo}': ^50}')
    
    print()
    print(f'{'< BOA SORTE! >':=^50}', end='\n\n')