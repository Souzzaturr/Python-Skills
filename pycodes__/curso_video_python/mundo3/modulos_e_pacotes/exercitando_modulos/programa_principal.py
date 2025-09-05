#Importações
import moeda

#---

preco = float(input("Digite um preço: R$"))


print(f"A metade de {moeda.formatar_valor(preco)} é {moeda.metade(preco, True)}")

print(f"O dobro de {moeda.formatar_valor(preco)} é {moeda.dobro(preco, True)}")

print(f"Aumentando 10% de {moeda.formatar_valor(preco)}, temos {moeda.aumentar(preco, 10, True)}")

print(f"Diminuindo 13% de {moeda.formatar_valor(preco)}, temos {moeda.diminuir(preco, 13, True)}")