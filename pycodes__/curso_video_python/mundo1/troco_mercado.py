print('----------------------------------')
n1 = int(input('total a pagar:'))
n2 = int(input('valor pago:'))
print(' ')

resto = n2 - n1

print(f'troco de R${resto}')
print(' ')

#divisao 100
divi_sem_sobra_100 = resto // 100

resto_divi_100 = resto % 100


#divisao 50
divi_sem_sobra_50 = resto_divi_100 // 50

resto_divi_50 = resto_divi_100 % 50


#divisao 20
divi_sem_sobra_20 = resto_divi_50 // 20

resto_divi_20 = resto_divi_50 % 20


#divisao 10
divi_sem_sobra_10 = resto_divi_20 // 10

resto_divi_10 = resto_divi_20 % 10


#divisao 2
divi_sem_sobra_2 = resto_divi_10 // 2

resto_divi_2 = resto_divi_10 % 2


#mensagem final de troco
print(f'providenciar troco de:')
print(' ')
print(f'{divi_sem_sobra_100} notas de R$100')
print(' ')
print(f'{divi_sem_sobra_50} notas de R$50')
print(' ')
print(f'{divi_sem_sobra_20} notas de R$20')
print(' ')
print(f'{divi_sem_sobra_10} notas de R$10')
print(' ')
print (f'{divi_sem_sobra_2} notas de R$2')
print(' ')
print(f'{resto_divi_2} moeda de R$1')
print(' ')
print('----------------------------------')
