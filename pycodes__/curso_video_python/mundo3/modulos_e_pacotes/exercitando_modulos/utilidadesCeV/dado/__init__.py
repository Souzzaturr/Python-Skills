#Módulo com funções de dados

def eh_float (caracteres: str) -> bool:
    """Recebe -> um conjunto de caracteres do timpo string;
    Verificação: SE esse caractere é um número OU se tem mais de 1 caractere E (caso negativo: se há apenas 1 sinal "-" E esse sinal é o primeiro caractere E o resto dos caracteres excluindo ponto e virgula, são numéricos) OU (se positivo: se não há sinal "-" e o resto dos caracteres excluindo ponto e virgula, são numéricos) E se há ponto e virgula, (apenas um, e ou só ponto ou só virgula) OU não tem nem ponto nem vírgula.;
    Retorna -> Um valor booleano [True/False]."""

    caracteres = caracteres.replace(" ", "")

    verificacao = (caracteres.isnumeric() or len(caracteres) > 1 and (("-" in caracteres and caracteres.count("-") == 1 and caracteres[0] == "-" and caracteres[1:].replace(".", "").replace(",", "").isnumeric()) or (not "-" in caracteres and caracteres.replace(".", "").replace(",", "").isnumeric())) and ((caracteres.count(".") == 1 and caracteres.count(",") == 0) or (caracteres.count(",") == 1 and caracteres.count(".") == 0) or (caracteres.count(".") == 0 and caracteres.count(",") == 0)))

    return verificacao



def transformar_dados_monetarios (numero: str) -> float:
    """Recebe -> string de número float com alguns caracteres não conhecidos pelo python como pertencentes a um número float;
    Tratamento: remove espaços e troca virgula por ponto.
    Retorna -> Um número float"""
    
    numero = numero.replace(" ", "").replace(",", ".")

    return float(numero)