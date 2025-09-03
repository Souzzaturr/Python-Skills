#Funções
def maior (lista_numeros) -> float:
    """Recebe uma lista com uma quantidade indeterminada de números.
    Retorna -> Maior número entre os que foram recebidos."""
    maior = lista_numeros[0]
    for numero in lista_numeros[1:]:
        if numero > maior:
            maior = numero
    return maior


def menor (lista_numeros) -> float:
    """Rebebe uma lista com uma quantidade indeterminada de núemros.
    Retorna -> Menor número entre os que foram recebidos."""
    menor = lista_numeros[0]
    for numero in lista_numeros[1:]:
        if numero < menor:
            menor = numero
    return menor


def media (lista_numeros) -> float:
    """Recebe uma lista com uma quantidade indetermina de números (no mínimo 1 número).
    Retorna -> Média dos valores recebidos."""
    soma = 0
    for numero in lista_numeros:
        soma += numero
    return soma/len(lista_numeros)


def relatorio_turma (notas, sit = False) -> dict:
    """Recebe uma lista com uma uma quantidade indeterminada de notas e um ultimo valor 'sit', que é opcional. 'True' indicando se deseja retornar a situação da turma (Muito boa, Boa, Regular, Ruim, Muito ruim), e 'False' se não desejar.
    Retorna -> Um dicionário contendo chaves com a quantidade de notas analisadas, a maior nota, a menor nota, a média de todas as notas, e se solicitado, a situação da turma."""

    relatorio = dict()

    #Armazena quantidade de notas
    relatorio["quantidade_notas"] = len(notas)

    #Calcula e armazena maior nota
    relatorio["maior_nota"] = maior(notas)

    #Calcula e armazena menor nota
    relatorio["menor_nota"] = menor(notas)

    #Calcula e armazena média das notas
    relatorio["media_notas"] = media(notas)

    #Armazena a situação da turma (Muito boa 10, 9), (Boa 8, 7), (Regular 6), (Ruim 5, 3), (Muito ruim 3, 0)
    if sit:
        if relatorio["media_notas"] >= 9:
            relatorio["situacao_turma"] = f"\033[32mMuito Boa\033[m"
        
        else:
            if relatorio["media_notas"] >= 7:
                relatorio["situacao_turma"] = f"\033[32mBoa\033[m"
            
            else:
                if relatorio["media_notas"] >= 6:
                    relatorio["situacao_turma"] = f"\033[33mRegular\033[m"
                
                else:
                    if relatorio["media_notas"] >= 3:
                        relatorio["situacao_turmas"] = f"\033[31mRuim\033[m"
                    
                    else:
                        relatorio["situacao_turmas"] = f"\033[31mMuito ruim\033[m"
    
    return relatorio


#Programa principal

print(help(relatorio_turma))

lista_notas = list()

qtd_notas_a_registrar = int(input("Quantidade de alunos: "))

for i in range(qtd_notas_a_registrar):
    nota = float(input(f"{i + 1}ª nota: "))
    lista_notas.append(nota)

situacao = input("Exibir situação da turma? [S/N] ").upper()[0]

for categoria, valor in relatorio_turma(lista_notas, sit = situacao == "S").items():
    print(f"{categoria} -> \033[33m{valor}\033[m")