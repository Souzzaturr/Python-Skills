#funções
def ficha_jogador (nome = "<desconhecido>", gols = 0) -> str:
    """Recebe o nome de um jogador 'nome' e a quantidade de gols feitos por esse jogador 'gols';
    Nome: uma string, se não for especificado um valor para nome, seu valor será '<desconhecido>';
    Gols: número natural, se não for espcificado, seu valor será 0;
    Retorna -> uma string apresentando o jogador e sua quantidade de gols feitos."""
    return f"O jogador {nome if nome else "<desconhecido>"} fez {gols if gols.isnumeric() else 0} gol(s) no campeonato!!"

#programa principal
print(help(ficha_jogador))

nome = input("Nome do jogador: ")
qtd_gols = input("Quantidade de gols: ")

print(ficha_jogador(nome, qtd_gols))