#Funções
def idade_valida (idade: int) -> bool:
    """Recebe -> Um número do tipo inteiro que representa uma idade;
    Retorna -> Um valor booleano [True] se for válido, se não, [False]."""

    #considera recém nascidos e pessoas muito velhas
    return idade >= 0 and idade <= 110