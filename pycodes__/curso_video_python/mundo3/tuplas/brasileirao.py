times = (
    "Flamengo",
    "Palmeiras",
    "São Paulo",
    "Corinthians",
    "Santos",
    "Grêmio",
    "Internacional",
    "Cruzeiro",
    "Atlético Mineiro",
    "Vasco da Gama",
    "Fluminense",
    "Botafogo",
    "Athletico Paranaense",
    "Bahia",
    "Fortaleza",
    "Sport Recife",
    "Coritiba",
    "Ceará",
    "Goiás",
    "Chapecoense"
    )

print('A) Os cinco primeiros colocados são:\n')

for time in times[:5]:
    print('->', time)


print('-' * 45)

print('B) Os ultimos quatro colocados da tabela são:\n')

for time in times[-4:]:
    print('->', time)


print('-' * 45)

print('C) Uma lista com os times em ordem alfabética:\n')

ordem = sorted(times)

for time in ordem:
    print(time)


print('-' * 45)

print('D) posição do time da chapecoense:\n')

posicao = times.index('Chapecoense')

print('nº', posicao)
