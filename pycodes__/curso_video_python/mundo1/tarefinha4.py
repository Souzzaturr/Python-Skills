#custo de viagem
distancia = int(input('Quantos quilometros você pretende andar em nossos ônibus?\n'))

if distancia <= 200:
    print(f'Preço da passagem (por km) é R${distancia * 0.5}')

else:
    print(f'Preço da passagem com desconto de 10% (por km) é R${distancia * 0.45}')

print('Boa viagem!')
