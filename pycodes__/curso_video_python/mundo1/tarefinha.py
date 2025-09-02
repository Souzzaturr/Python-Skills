#jogo da adivinhação
print('Olá, quer jogar um jogo? :)')
resposta = input().lower().strip()

if resposta == 'sim' or resposta == 's':
    print('Esta bem!!')
    print('O jogo é o seguinte:')
    print('Eu irei pensar em um numedo de 1 a 5')
    print('E você vai ter que adivinhar que número é esse.')
    print('Vamos começar:')

    import random
    numero_pensado = random.randint(1,5)

    print('Acabei de pensar em um número!!')
    print('Consegue adivinha-lo? qual é o numero?')
    numero_chutado = int(input())

    if numero_chutado == numero_pensado:
        print('Parabéns, você acertou o número!!')
        print(f'O número pensado é {numero_pensado}😁')
        
    else:
        print('Você errou!!')
        print(f'O número é {numero_pensado}😥')
        
else:
    print('Acho que você não está a fim de jogar agora, então até a proxima!!')

print('--FIM DE JOGO--')
