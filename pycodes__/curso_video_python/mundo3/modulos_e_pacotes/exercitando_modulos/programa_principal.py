#Importações
from utilidadesCeV import moeda, dado

#---

preco = input("Digite um preço: R$")

while not dado.eh_float(preco):
    print(f'\033[1;31mERRO! "{preco}" não é um número válido!!\033[m')

    preco = input("Digite um preço VÁLIDO: ")

preco = dado.transformar_dados_monetarios(preco)


moeda.resumo(preco, 80, 35)