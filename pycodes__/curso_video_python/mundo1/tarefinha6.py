#comparacao maior e menor numero
print('Vamos jogar um jogo!')
print('Você me fala 3 numeros diferentes e eu lhe digo qual deles é o maior e qual é o menor')
n1 = int(input('Digite o primeiro número abaixo.\n'))
n2 = int(input('Digite o segundo número abaixo.\n'))
n3 = int(input('Digite o terceito número abaixo.\n'))

#maior numero
if n1 > n2 and n1 > n3:
    print(f'Número {n1} é o maior número!')

elif n2 > n1 and n2 > n3:
    print(f'Número {n2} é o maior número!')

elif n3 > n1 and n3 > n2:
    print(f'Número {n3} é o maior número!')

else:
    print('Todos ou alguns são iguais, logo não há um número que seja maior que os demais.')

#menor numero
if n1 < n2 and n1 < n3:
    print(f'Número {n1} é o menor número!')

elif n2 < n1 and n2 < n3:
    print(f'Número {n2} é o menor número!')

elif n3 < n1 and n3 < n2:
    print(f'Número {n3} é o menor número!')

else:
    print('Todos ou alguns são iguais, logo não há um numero que seja menor que os demais.')

print('--FIM--')