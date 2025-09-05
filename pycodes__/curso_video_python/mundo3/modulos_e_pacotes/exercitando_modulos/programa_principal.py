#Importações
import moeda

#---

preco = float(input("Digite um preço: R$"))


print(f"A metade de {preco} é {moeda.metade(preco)}")

print(f"O dobro de {preco} é {moeda.dobro(preco)}")

print(f"Aumentando 10% de {preco}, temos {moeda.aumentar(preco, 10)}")

print(f"Diminuindo 13% de {preco}, temos {moeda.diminuir(preco, 13)}")