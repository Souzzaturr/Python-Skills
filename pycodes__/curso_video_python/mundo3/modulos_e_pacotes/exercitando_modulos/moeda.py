#Módulo com funções de moedas

def aumentar (valor: float, percentual = 50.0) -> float:
    """Recebe -> um valor float qualquer;
    Valor: valor a ser aumentado;
    Percentual: percentual a ser acrescido à valor (padrão é 50%);
    Retorna -> o valor acrescido da porcentagem escolhida."""
    return valor + valor * percentual/100
    


def diminuir (valor: float, percentual = 50.0) -> float:
    """Recebe -> um valor float qualquer;
    Valor: valor a ser diminuido;
    Percentual: percentual a ser subtraido de valor;
    Retorna -> porcentagem restante do valor."""
    return valor * (1.0 - percentual/100)



def dobro (valor: float) -> float:
    """Recebe -> um valor float qualquer;
    Retorna -> o dobro desse valor."""
    return valor * 2



def metade (valor: float) -> float:
    """Recebe -> um valor float qualquer;
    Retorna -> A metade desse valor."""
    return valor / 2



def formatar_valor (valor: float) -> str:
    """Recebe -> um valor float qualquer;
    Valor: um número inteiro qualquer;
    Retorna -> Uma string no seguinte formato: R$valor.00"""
    return f"R${valor:.2f}"