#Importações
import moeda

#---

preco = float(input("Digite um preço: R$"))


print(f"A metade de {moeda.formatar_valor(preco)} é {moeda.formatar_valor(moeda.metade(preco))}")

print(f"O dobro de {moeda.formatar_valor(preco)} é {moeda.formatar_valor(moeda.dobro(preco))}")

print(f"Aumentando 10% de {moeda.formatar_valor(preco)}, temos {moeda.formatar_valor(moeda.aumentar(preco, 10))}")

print(f"Diminuindo 13% de {moeda.formatar_valor(preco)}, temos {moeda.formatar_valor(moeda.diminuir(preco, 13))}")