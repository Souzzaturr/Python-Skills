#Funções
def bloco_cabecalho (msg: str) -> str:
    """Recebe uma string qualquer.
    Retorna -> Um bloco ao redor da string recebida."""
    bloco = "+" + "-" * (len(msg) + 8) + f"+\n"
    bloco += f"|    {msg}    |\n"
    bloco += "+" + "-" * (len(msg) + 8) + "+"
    return bloco

#Código principal

while True:
    print(f"\033[1;32m{bloco_cabecalho('SISTEMA DE AJUDA PyHELP')}\033[m")

    comando = input("Função ou Biblioteca -> ")

    if comando.upper() == "FIM":
        print(f"\033[1;31m{bloco_cabecalho('Programa finalizado.')}\033[m")
        break

    print(f"\033[1;38m{bloco_cabecalho(f'Acessando manual do comando/biblioteca {comando}')}\033[m")

    print(f"\033[33m{help(comando)}\033[m")

