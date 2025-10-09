from pilha_class import Pilha
from no_class import No

print("\n--- Pilha ---")

arturo_pilhas = Pilha()

while True:
    print("""
[ 1 ] Adicionar números
[ 2 ] Remover números
[ X ] Sair
""")
    
    resposta = input("Escolha uma ação: \n")

    if resposta == "1":
        valor = input("Digite um número qualquer: \n")

        arturo_pilhas.empilhar(No(valor))

        print(f"Valor {arturo_pilhas.topo} adicionado com sucesso!!")
    
    else:
        if resposta == "2":
            if arturo_pilhas.tah_vazio():
                print("Pilha está vazia...")

            else:
                valor = arturo_pilhas.desempilhar()

                print(f"valor {valor} foi desempilhado com sucesso da pilha!!")
        
        else:
            break
    
    print(f"Pilha: {arturo_pilhas}")

print(f"Estado final Pilha: {arturo_pilhas}")