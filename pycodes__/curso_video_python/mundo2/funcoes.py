def eh_par (x: int) -> bool:
    return x % 2 == 0


def soma (lista: list) -> int:
    soma = 0
    
    for i in range(len(lista)):
        soma = soma + lista[i]
    
    return soma

def int_valido (x: int) -> bool:
    return x.isnumeric()

def homi_muie (sexo: str) -> bool:
    return sexo == 'H' or sexo == 'M'

def verifica_resposta (resposta: str) -> bool:
    return resposta == 'S' or resposta == 'N'