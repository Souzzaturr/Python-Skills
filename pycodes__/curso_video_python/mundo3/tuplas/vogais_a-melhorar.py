def vogal (palavra: str) -> str:
    vogais_em_palavra = tuple()
    vogais = 'aeiouAEIOU'
    for letra in palavra:
        if letra in vogais:
            vogais_em_palavra = vogais_em_palavra + tuple(letra)
    return vogais_em_palavra

print(vogal('Artur'))