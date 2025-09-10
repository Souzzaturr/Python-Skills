#Funções
def bloco (menssagem: str) -> str:
    """Recebe -> uma menssagem;
    Retorna -> um bloco contendo essa mensagem dentro."""

    largura_bloco = 50 if len(menssagem) <= 50 else (len(menssagem) + 10)

    bloco_menssagem = "+" + "-" * largura_bloco + "+\n"
    bloco_menssagem += "|" + menssagem.center(largura_bloco) + "|\n"
    bloco_menssagem += "+" + "-" * largura_bloco + "+"

    return bloco_menssagem



def opcoes () -> str:
    """Retorna -> um menu com 3 opções (adicionar, excluir, ou sair de um programa)."""

    print(f"\033[1;33m1\033[m - \033[1;36mVer pessoas cadastradas\033[m")
    print(f"\033[1;33m2\033[m - \033[1;36mCadastrar nova pessoa\033[m")
    print(f"\033[1;33m3\033[m - \033[1;36mSair do programa\033[m")

    return



def exibir_pessoas () -> str:
    """Retorna -> Uma tabela contendo nome de pessoas cadastradas e suas respectivas idades."""

    from . import dado

    tabela = str()

    for nome, idade in dado.ler_banco_dados():
        tabela += f"     {nome}     \t{idade} anos\n"
    
    return tabela