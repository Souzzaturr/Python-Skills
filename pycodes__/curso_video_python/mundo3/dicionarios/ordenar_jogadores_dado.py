#Exercicios com dicionários]

import random

jogadores = dict()

jogadores["1"] = random.randint(0, 6)
jogadores["2"] = random.randint(0, 6)
jogadores["3"] = random.randint(0, 6)
jogadores["4"] = random.randint(0, 6)

for key, value in jogadores.items():
  print(f"Jogador {key} lançou o dado e caiu {value}")

print("\n", "-" * 50, "\n")

print(f"{'Ranking dos jogadores:':^50}\n")

ranking_jogadores = [[list(jogadores.keys())[0], list(jogadores.values())[0]]]

for key, value in list(jogadores.items())[1:]:

  for i in range(len(ranking_jogadores)):
    
    if jogadores[key] >= ranking_jogadores[i][1]:
      ranking_jogadores.insert(i, [key, value])
      break

    else:
      if i == len(ranking_jogadores) - 1:
        ranking_jogadores.append([key, value])


for i in range(len(ranking_jogadores)):
  print(f"{i + 1}º lugar -> Jogador {ranking_jogadores[i][0]} que tirou {ranking_jogadores[i][1]} no dado!!")