#Funções
def guardar_cadastro(nome: str, idade: int):
    """Recebe -> um nome de uma pessoa e sua idade, e guarda esses dados em um arquivo csv;
    nome: do tipo string;
    idade: do tipo inteiro;
    Retorna -> None"""

    nome = nome.replace(",", "")

    with open("pessoas_cadastradas.csv", "a", encoding = "UTF-8") as banco_de_dados:
        banco_de_dados.write(f"{nome},{idade}\n")
    
    return



def ler_banco_dados () -> list:
    """Retorna -> Uma lista onde cada elemento é uma lista contendo um nome do tipo string e uma idade do tipo float."""

    lista_cadastros = list()

    try:
        with open("pessoas_cadastradas.csv", "r", encoding = "UTF-8") as banco_de_dados:
            for cadastro in banco_de_dados.read().splitlines():
                lista_cadastros.append(cadastro.split(","))
    
    except FileNotFoundError:
        return [["Não há usuários cadastrados...", 000]]
    
    return lista_cadastros