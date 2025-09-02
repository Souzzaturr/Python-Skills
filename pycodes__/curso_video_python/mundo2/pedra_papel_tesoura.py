import random

lista_vitorias = [0, 0] #computador / jogador
rodadas = 0

print('Bem vindo ao jogo Pedra-Papel-tesoura!!')
print('Aqui, EU (computador) serei seu oponente >:)')
print('Vamos começar!!!\n')

while True:

    rodadas = rodadas + 1

    print(f'{rodadas}ª rodada!\n')

    print('''Tesoura == T 
   Pedra == P
   Papel == A
   Sair == X\n''') #T -> 1, P -> 2, A -> 3

    acao_jogador = input('Digite "T" ou "P" ou "A" para escolhe entre Tesoura, Pedra ou Papel, respectivamente. Para finalizar a brincadeira, digite "X".\n').strip().upper()

    while acao_jogador != 'T' and acao_jogador != 'P' and acao_jogador != 'A' and acao_jogador != 'X':

        print('Não entendi o que você quis dizer :(')

        acao_jogador = input('Poderia digitar novamente sua resposta?\n').strip().upper()

    if acao_jogador == 'X':
        break

    else:

        if acao_jogador == 'T':
            print('Você escolheu TESOURA\n')

        else:
            if acao_jogador == 'P':
                print('Você escolheu PEDRA\n')

            else:
                print('Você escoheu PAPEL\n')
                
        
        resposta_computador = random.randint(1, 3)

        if resposta_computador == 1:
            print('Computador escolheu TESOURA\n')

        else:
            if resposta_computador == 2:
                print('Computador escolheu PEDRA\n')

            else:
                if resposta_computador == 3:
                    print('Computador escolheu PAPEL\n')


        #a acabar
