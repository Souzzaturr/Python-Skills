#funções
def fatorial (num: int, show = False) -> int:
    """Recece um valor obrigatório 'num' e um opcional 'show';
    Num: Número natural;
    show: se True, exibe toda a operação, se False, não exibe;
    Retorna -> Fatorial de um número natural."""
    produto = num
    if show:
        operacao = str(produto) + " x "
    for i in range (num - 1, 1, -1):
        if show:
            operacao += f"{i} x " if i > 2 else f"{i} x 1 = "
        produto *= i
    if show:
        operacao += str(produto)
        return operacao
    return produto

#programa principal
print(help(fatorial))

numero = int(input("Número: "))

print(fatorial(numero, show = True))
print(fatorial(numero))