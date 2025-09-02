def soma_idades (pessoas: dict) -> float:
  soma = 0
  for pessoa in pessoas.keys():
    soma += pessoas[pessoa]["idade"]
  return soma

def mulheres_cadastradas (pessoas: dict) -> list:
  lista_mulheres = list()
  for pessoa in pessoas.keys():
    if pessoas[pessoa]["sexo"] == "F":
      lista_mulheres.append(pessoas[pessoa]["nome"])
  return lista_mulheres

def idades_acima_media (pessoas: dict) -> list:
  lista_acima_media = list()
  media_idades = soma_idades(pessoas)/len(pessoas.keys())
  for pessoa in pessoas.keys():
    if pessoas[pessoa]["idade"] > media_idades:
      lista_acima_media.append(pessoas[pessoa])
  return lista_acima_media

#Exercícios com dicionários

pessoas = dict()
resp = "S"

while resp == "S":

  print("\n", "-" * 50, "\n")

  nome = input("Nome: ")

  pessoas[nome] = dict()

  pessoas[nome]["nome"] = nome

  pessoas[nome]["sexo"] = input("Sexo [M/F]: ").upper()

  while pessoas[nome]["sexo"] != "M" and pessoas[nome]["sexo"] != "F":
    print("ERROR")
    pessoas[nome]["sexo"] = input("Digite apenas [M] para Masculino, ou [F] para Feminino: ").upper()

  pessoas[nome]["idade"] = input("Idade: ")

  while not pessoas[nome]["idade"].isnumeric() and (pessoas[nome]["idade"] < 0 or pessoas[nome]["idade"] > 120):
    print("ERROR")
    pessoas[nome]["idade"] = input("Digite uma idade válida (contendo apenas números, e que seja um número entre 0 e 120): ")
  
  pessoas[nome]["idade"] = int(pessoas[nome]["idade"])

  resp = input("Quer adicionar mais uma pessoa? [S/N]").upper()

  while resp != "S" and resp != "N":
    print("ERROR")
    resp = input("Digite apenas [S] para Sim, ou [N] para Não: ").upper()

print("\n", "-" * 50, "\n")

print(f"A) Ao todo, temos {len(pessoas.keys())} cadastradas!!\n")

print(f"B) A média das idades é de {soma_idades(pessoas)/len(pessoas.keys())} anos!!\n")

print(f"C) As mulheres cadastradas foram:")
for mulher in mulheres_cadastradas(pessoas):
  print(mulher)
print()

print(f"D) Lista das pessoas que tem idade acima da média ({soma_idades(pessoas)/len(pessoas.keys())}):")
for pessoa in idades_acima_media(pessoas):
  print(f"{pessoa['nome']}, do sexo [{pessoa['sexo']}], com {pessoa['idade']} anos!!")
print()

print(f"{'<Programa encerrado>':-^50}")