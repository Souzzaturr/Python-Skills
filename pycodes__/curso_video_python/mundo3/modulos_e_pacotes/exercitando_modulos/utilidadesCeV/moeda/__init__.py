#Módulo com funções de moedas

def aumentar (valor: float, percentual = 50.0, formatar = False) -> float | str:
    """Recebe -> um valor float qualquer, um percentual de quanto vai ser acrecentado ao valor, e um parametro formatar;
    Valor: valor a ser aumentado;
    Percentual: percentual a ser acrescido à valor (padrão é 50%);
    Formatar: retorna o valor formatado em 'R$valor.00' se True, ou sem formatação se False;
    Retorna -> o valor acrescido da porcentagem escolhida."""
    if formatar:
        return formatar_valor(valor + valor * percentual/100)
    return valor + valor * percentual/100
    


def diminuir (valor: float, percentual = 50.0, formatar = False) -> float | str:
    """Recebe -> um valor float qualquer, um percentual de quanto vai ser subtraido de valor, e um parametro formatar;
    Valor: valor a ser diminuido;
    Percentual: percentual a ser subtraido de valor;
    Formatar: retorna o valor formatado em 'R$valor.00' se True, ou sem formatação se False;
    Retorna -> porcentagem restante do valor."""
    if formatar:
        return formatar_valor(valor * (1.0 - percentual/100))
    return valor * (1.0 - percentual/100)



def dobro (valor: float, formatar = False) -> float | str:
    """Recebe -> um valor float qualquer, e um parametro formatar;
    Valor: valor a ser dobrado;
    Formatar: retorna o valor formatado em 'R$valor.00' se True, ou sem formatação se False;
    Retorna -> o dobro desse valor."""
    if formatar:
        return formatar_valor(valor * 2)
    return valor * 2



def metade (valor: float, formatar = False) -> float | str:
    """Recebe -> um valor float qualquer, e um parametro formatar;
    Valor: valor a ser dividido pela metade;
    Formatar: retorna o valor formatado em 'R$valor.00' se True, ou sem formatação se False;
    Retorna -> A metade desse valor."""
    if formatar:
        return formatar_valor(valor / 2)
    return valor / 2



def formatar_valor (valor: float) -> str:
    """Recebe -> um valor float qualquer;
    Valor: um número inteiro qualquer;
    Retorna -> Uma string no seguinte formato: R$valor.00"""
    return f"R${valor:.2f}"



def resumo (valor: float, aumento = 50.0, reducao = 50.0) -> str:
    """Recebe -> valor sendo um float qualquer, aumento representando o quanto vai aumentar, e redução representando o quanto vai diminuir;
    Valor: Float qualquer;
    Aumento: O tanto (em porcentagem) a ser adicionado a valor;
    Reducao: O tanto (em porcentagem) a ser subtraido de valor;
    Retorna -> Um painel exibindo o valor recebido, o dobro do valor, a metade do valor, o aumento do valor, e a redução do valor."""
    print("-" * 50)
    print(f"{'RESUMO DO VALOR': ^50}")
    print("-" * 50)
    print(f"{f'Preço analisado:          {formatar_valor(valor)}': ^50}")
    print(f"{f'Dobro do preço:           {dobro(valor, True)}': ^50}")
    print(f"{f'Metade do preço:          {metade(valor, True)}': ^50}")
    print(f"{f'{aumento}% de aumento:           {aumentar(valor, aumento, True)}': ^50}")
    print(f"{f'{reducao}% de redução:           {diminuir(valor, reducao, True)}': ^50}")
    print("-" * 50)