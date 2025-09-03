#funções
def voto (num: int) -> str:
    """Recebe um número entre 0 e 100 que representa uma idade;
    Se menor que 16, retorna 'NÃO VOTA';
    Se maior que 16 e menor que 65, retorna 'VOTO OBRIGATÓRIO';
    Se maior que 65, retorna 'VOTO OPIONAL."""
    if num < 16:
        return "\033[1;33mNÃO VOTA\033[m"
    
    if num >= 16 and num < 65:
        return "\033[1;31mVOTO OBRIGATÓRIO\033[m"
    
    if num >= 65:
        return "\033[1;32mVOTO OPCIONAL\033[m"

#código principal

print(help(voto))

idade = int(input("Digite sua idade: "))

print(f"Sua situação eleitoral é a seguinte: {voto(idade)}")