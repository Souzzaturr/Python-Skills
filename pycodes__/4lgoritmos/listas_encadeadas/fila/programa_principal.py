from no_class import No
from fila_class import Fila

print("\n--- Fila ---")

arturo_filas = Fila()

while True:
    print("""
[ 1 ] Adicionar números
[ 2 ] Remover números
[ 3 ] Tamanho da fila
[ X ] Sair
""")
    
    resposta = input("Escolha uma ação: \n")

    if resposta == "1":
        valor = input("Digite um número qualquer: \n")

        arturo_filas.adiciona(No(valor))

        print(f"Valor {arturo_filas.exibir_inicio} adicionado com sucesso!!")
    
    else:
        if resposta == "2":
            if arturo_filas.tah_vazio:
                print("Fila está vazia...")

            else:
                valor = arturo_filas.remove()

                print(f"valor {valor} foi removido com sucesso da fila!!")
        
        else:
            if resposta == "3":
                print(f"O tamanho atual da Fila é: {arturo_filas.tamanho}")

            else:
                break

    print()
    print(f"Inicio da Fila: {arturo_filas.exibir_inicio}")
    print(f"Fim da fila: {arturo_filas.exibir_fim}")
    print(f"Fila => {arturo_filas}")

print(f"Estado final da Fila: {arturo_filas}")