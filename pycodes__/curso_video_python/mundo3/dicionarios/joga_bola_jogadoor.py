#Exercícios com dicionários

jogador = dict()

jogador["nome"] = input("Nome: ")

jogador["partidas"] = list()

n_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

jogador["gols"] = 0

for i in range(n_partidas):
  gols = int(input(f"Quantos gols {jogador['nome']} fez na {i + 1}ª partida? "))
  jogador["partidas"].append(gols)
  jogador["gols"] += gols

print("\n", "-" * 50, "\n")

print(jogador)

print("\n", "-" * 50, "\n")

for keys in jogador.keys():
  print(f"O campo {keys} tem valo de {jogador[keys]}")

print("\n", "-" * 50, "\n")

print(f"O jogador {jogador['nome']} fez:")

for indice, gols in enumerate(jogador['partidas']):
  print(f"{gols} gols na {indice + 1}ª partida.")

print(f"Sendo um total de {jogador['gols']} gols!!")