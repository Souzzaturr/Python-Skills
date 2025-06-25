#--funcoes--
def somador (lista: list) -> float:
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    return soma

def subtracao (lista: list) -> float:
    subtracao = lista[0]
    for i in range(1, len(lista)):
        subtracao = subtracao - lista[i]
    return subtracao

def multiplicador (lista: list) -> float:
    produto = 1
    for i in range(len(lista)):
        produto = produto * lista[i]
    return produto

def divisor (lista: list) -> float:
    divisao = lista[0]
    for i in range(1, len(lista)):
        if lista[i] != 0:
            divisao = divisao / lista[i]
        else:
            divisao = 'ERRO, IMPOSSÍVEL DIVIDIR POR ZERO!'
            break
    return divisao

def maior (lista: list) -> float:
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

def menor (lista: list) -> float:
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

#--funcoes especificas--
def resposta_numero (x: str) -> float:
    x = x.replace(' ', '')
    negativo = False
    while True:
        if '-' in x:
            negativo = x[0] == '-'
        ponto_flutuante = x.count('.') == 1
        if negativo:
            x = x[1:]
        if ponto_flutuante:
            posicao_ponto = x.find('.')
            x = x.replace('.', '')
        if x.isnumeric():               #<-condicao de parada
            break
        else:
            x = input('Digite APENAS números!\n').replace(' ', '')
    if ponto_flutuante:
        if posicao_ponto == 0:
            x = '0' + '.' + x
        else:
            if posicao_ponto == len(x):
                x = x + '.' + '0'
            else:
                x = x[0:posicao_ponto] + '.' + x[posicao_ponto:]
    if negativo:
        x = '-' + x
    return float(x)

def mostrar_operacao_completa (simbolo: str, lista: list, resultado: float) -> str:
    operacao = str(lista[0]) + ' '
    for i in range(1, len(lista)):
        operacao = operacao + simbolo + ' ' + str(lista[i]) + ' '
    operacao = operacao + '=' + ' ' + str(resultado)
    return operacao

#--codigo principal--
resposta = 0

while True:
    lista_numeros = list()

    print('-'*60)
    print('CALCULADOR\n')
    print('Preciso de pelo menos 2 números.')

    for i in range(2):
        numero = resposta_numero(input('Digite um número.\n'))
        
        lista_numeros.append(float(numero))

    print('''
Ações:
          
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR & MENOR
    [6] DIGITAR MAIS NÚMEROS
    [7] SAIR DO PROGRAMA
              ''')
    
    resposta = resposta_numero(input('Escolha uma ação.\n'))

    while resposta < 1 or resposta > 7:
        resposta = resposta_numero(input('Por favor, escolha apenas números entre 1 e 5 (incluindo o 1 e o 5)\n'))
    
    while resposta == 6:
        lista_numeros.append(resposta_numero(input('Digite mais um número.\n')))

        print('''
Ações:
          
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR & MENOR
    [6] DIGITAR MAIS NÚMEROS
    [7] SAIR DO PROGRAMA
              ''')

        resposta = resposta_numero(input('Escolha uma ação.\n'))

        while resposta < 1 or resposta > 7:
            resposta = resposta_numero(input('Por favor, escolha apenas números entre 1 e 5 (incluindo o 1 e o 5)\n'))
    
    if resposta == 1:
        soma = somador(lista_numeros)
        print(f'A soma de todos os números digitados é: {soma}')
        print(mostrar_operacao_completa('+', lista_numeros, soma))
    
    if resposta == 2:
        subtracoes = subtracao(lista_numeros)
        print(f'A subração de todos os números sucessivamente é: {subtracoes}')
        print(mostrar_operacao_completa('-', lista_numeros, subtracoes))
    
    if resposta == 3:
        produto = multiplicador(lista_numeros)
        print(f'O produto de todos os números digitados é: {produto}')
        print(mostrar_operacao_completa('x', lista_numeros, produto))
    
    if resposta == 4:
        divisao = divisor(lista_numeros)
        print(f'A divisão de todos os números sucessivamente é aproximadamente: {divisao}')
        print(mostrar_operacao_completa('÷', lista_numeros, divisao))

    if resposta == 5:
        print(f'Maior número digitado foi: {maior(lista_numeros)}')
        print(f'Menor número digitado foi: {menor(lista_numeros)}')
    
    if resposta == 7:
        print('FINALIZANDO...')
        break
#--FIM--