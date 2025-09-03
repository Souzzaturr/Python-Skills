#funcoes
def fatorial (num = 1) -> int:
    """Recebe um valor inteiro;
    Retorna -> Seu fatorial (n x n-1 x n-2 x n-3 ... 1)"""
    if num == 1:
        return num
    
    produto = num * fatorial(num - 1)

    return produto

#codigo principal
print(fatorial(5))

print(help(fatorial))