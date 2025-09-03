#funções
def validador_entrada (menssagem = "Digite um número inteiro qualquer: ") -> int:
    """Recebe uma string como entrada, e verifica se essa string é um número ou não.
    Valor: uma string, que pode representar um número inteiro;
    Retorna -> Uma menssagem sinalizando se o valor é válido ou não, se não for, será solicitado um novo valor."""
    valor = input(menssagem)
                #se for positivo (sem sinal "-") ou se for negativo (com sinal "-")
    while not (valor.isnumeric() or len(valor) > 1 and valor[0] == "-" and valor[1:].isnumeric()):
        print("\033[1;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!!\033[m")
        valor = input(menssagem)
    return int(valor)

#programa principal
print(help(validador_entrada))

numero = validador_entrada("Digite um número: ")
print(f"\033[1;32mVocê acabou de digitar o número \033[33m{numero}\033[m")