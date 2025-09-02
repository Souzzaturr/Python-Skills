#soma de todos os numeros ate x

x = 1
numero = 1
quantidade_escolhida = int(input('Digite apenas um numero inteiro positivo qualquer 😏\n'))
quantidade_escolhida2 = quantidade_escolhida

while(numero < quantidade_escolhida):
    numero = numero + 1
    x = x + numero

print(f'A soma de todos os numeros de 1 até {quantidade_escolhida2} é:\n{x}')
