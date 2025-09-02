import funcoes
import random

while True:
    num = int(input())
    
    if num < 0 or num > 10:
        break

    resp_jogador = input().upper()
    computador = random.randint(0, 10)
    print(f'Computador escolhe {computador}')

    impar_par = funcoes.eh_par(num + computador)
    
    if impar_par:
        resultado = 'PAR'
    
    else:
        resultado = 'IMPAR'


    if resultado != resp_jogador:
        print('Poxa, que pena, você perdeu >:)')
    
    else:
        print('Parabéns, você ganhou essa partida!!!')