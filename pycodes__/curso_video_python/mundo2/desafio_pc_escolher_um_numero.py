import random

print('Vamos jogar um jogo?')

while True:

    print('Eu (Conputador) pensarei em um número e você terá que adivinhar')
    print('Darei algumas dicas ao longo do jogo')
    start_stop = str(input('Vamos começar? Digite "S" para jogar, "N" para sair.\n').strip().upper())

    while start_stop != 'S' and start_stop != 'N':
        print('Não entendi...')
        start_stop = str(input('Poderia digitar novamente? "S" para SIM, "N" para NÂO.\n').strip().upper())
    
    if start_stop == "N":
        print('Saindo...')
        break

    print('Vamos começar!!!')

    num_pc = random.randint(1, 10)

    print('Pensei em um número entre 1 e 10 (incluindo 1 e 10)')
    print('Qual será?')

    num_jogador = str(input('Algum chute?\n').strip())

    tentativas = 0

    while not num_jogador.isnumeric() or int(num_jogador) < 1 or int(num_jogador) > 10:
        print('Não entendi...')
        num_jogador = str(input('Chute um NÚMERO entre 1 e 10 (incluindo 1 e 10)\n').strip())

    while int(num_jogador) != num_pc:
        tentativas = tentativas + 1
        print(f'Errou, não pensei no número {num_jogador}')
        num_jogador = str(input('Tente novamente!\n').strip())
    
        while not num_jogador.isnumeric() or int(num_jogador) < 1 or int(num_jogador) > 10:
            print('Não entendi...')
            num_jogador = str(input('Chute um NÚMERO entre 1 e 10 (incluindo 1 e 10)\n').strip())

    print('Parabéns, você acertou o número que eu pensei!!!')
    print(f'Eu pensei no número {num_pc}')
    print(f'E você chutou {num_jogador}')
    print(f'Você precisou de {tentativas} tentativas!!')