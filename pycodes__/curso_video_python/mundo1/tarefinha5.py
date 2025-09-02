#ano bissexto
print('Quer saber que ano é um ano bissexto??')
ano = int(input('Digite abaixo.\n'))

if (ano % 4) == 0 or (ano % 400) == 0:
    print(f'{ano} é um ano bissexto!')

else:
    print(f'{ano} não é um ano bissexto!')

print('--FIM--')