#entrada de dados
print('-=-' * 20)
reta_1 = float(input('Digite abaixo uma reta\n')) #primeira reta
reta_2 = float(input('Digite abaixo outra reta\n')) #segunda reta
reta_3 = float(input('Digite abaixo outra reta\n')) #terceira reta
print('-=-' * 20)

#comparação
resultado = reta_1 + reta_2 > reta_3 and reta_2 + reta_3 > reta_1 and reta_1 + reta_3 > reta_2

if resultado == True:
    print(f'Dá pra fazer um triângulo com as retas {reta_1}, {reta_2} e {reta_3}!!')

else:
    print(f'Não dá pra fazer um triângulo com as retas {reta_1}, {reta_2} e {reta_3}!!')

print('-=-' * 7, 'FIM DE CÓDIGO', '-=-' * 8)
