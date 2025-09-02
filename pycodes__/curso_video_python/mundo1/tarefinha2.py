#SEMOB CODE
velocidade = int(input('DIGITE ABAIXO A VELOCIDE DO VEÍCULO (EM KM/H)\n'))

if velocidade > 80:
    print('VEÍCULO SERÁ MULTADO POR EXCESSO DE VELOCIDADE 🚨')
    print('O VALOR DA MULTA SERÁ DADO CONFORME O QUE FOI EXCEDIDO DO LIMITE MÁXIMO DA VIA')

    valor_multa = (velocidade % 80) * 7

    print(f'COBRAR MULTA DE R${valor_multa}')

else:
    print('TUDO EM ORDEM, PODE LIBERAR 👍')

print('--FIM--')
