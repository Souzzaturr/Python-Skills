#Funções

def fatorial (num: int) -> int:
    """Recebe um número inteiro.
    Retorna -> o fatorial do número recebido."""
    
    produto = num

    for i in range(num - 1, 1, -1):
        produto *= i
    
    return produto