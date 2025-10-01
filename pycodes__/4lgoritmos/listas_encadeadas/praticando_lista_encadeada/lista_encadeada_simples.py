#Botando em prática minha lógica recém adiquirida de listas encadeadas :)
#Neste algoritmo, cada nó recebe uma lista com espaço para dois elementos. [valor, prox_endereco]

lista_encadeada = [0, None]
valor = 0
resposta = "s"

print("--- Lista encadeada ---")

while resposta.upper() == "S":
    print("Digite um valor:")
    valor = int(input())

    no = [valor, None]
    temp = lista_encadeada

    while temp[1] != None:
        temp = temp[1]
    
    temp[1] = no

    resposta = input("Deseja continuar? [s/n]")

print("Os valores digitados foram:")

temp = lista_encadeada

print(temp[0], end = ", ")

while temp[1] != None:
    temp = temp[1]
    print(temp[0], end = ", ")

print()