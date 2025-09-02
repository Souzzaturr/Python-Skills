#aumento de salários
print('A empresa está crescendo!')
print('Para ninguem ficar para trás, todos os funcionários terão um aumento!!')
print('Para salários de até R$1.250; terão um aumento de 15%!!')
print('Para os salários superiores a R$1.250; um aumento de 10%!!')
salario = float(input('Vamos simular o seu aumento, digite abaixo seu salário\n'))

if salario <= 1250:
    print(f'Seu novo salário com o aumento será de R${salario * 1.15}')
    print(f'Tendo um aumento de R${salario * 0.15}')

else:
    print(f'Seu novo salário será de R${salario * 1.1}')
    print(f'Tendo um aumento de R${salario * 0.1}')

print('--FIM--')