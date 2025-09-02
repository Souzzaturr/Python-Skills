#Exercicios com dicionários

print("\n", "-" * 50, "\n")

trabalhador = dict()

trabalhador["Nome"] = input("Nome: ")

trabalhador["Nascimento"] = int(input("Ano de nascimento: "))

trabalhador["Carteira"] = int(input("Nº da CLT (0 se não tiver): "))

if trabalhador["Carteira"] != 0:
  trabalhador["Ano contratacao"] = int(input("Ano de contratação: "))
  trabalhador["Salario"] = float(input("Salário: "))

  ano_aposentadoria = trabalhador["Ano contratacao"] + 35 - trabalhador["Nascimento"]

print("\n", "-" * 50, "\n")

for key in trabalhador.keys():
  print(f"{key} tem valor de {trabalhador[key]}.")

if trabalhador["Carteira"] != 0:
  print(f"{trabalhador['Nome']} irá se aposentar com {ano_aposentadoria} anos.")