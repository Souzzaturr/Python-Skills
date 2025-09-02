import funcoes

resposta = ''
lista_idades = list()
homen_mulher = [0, 0]
mulheres_menores_20 = 0

while resposta != 'N':
    print('---' * 15)
    idade = input('Digite uma idade.\n')

    while not funcoes.int_valido(idade):
        idade = input()
    idade = int(idade)

    lista_idades.append(idade)

    sexo = input('Digite o sexo (H para Homem, M para Mulher).\n').upper()
    
    while not funcoes.homi_muie(sexo):
        sexo = input().upper()
    
    if sexo == 'H':
        homen_mulher[0] = homen_mulher[0] + 1

    else:
        homen_mulher[1] = homen_mulher[1] + 1
        if idade <= 20:
            mulheres_menores_20 = mulheres_menores_20 + 1
    
    resposta = input('Quer continuar? (s/n)\n').upper()

    while not funcoes.verifica_resposta(resposta):
        resposta = input().upper()

maiorais = 0

for idade in lista_idades:
    if idade > 18:
        maiorais = maiorais + 1

print(f'A) {maiorais} pessoas são de maiores.')

print(f'B) {homen_mulher[0]} homens foram cadastrados.')

print(f'C) {mulheres_menores_20} mulheres tem idades iguais ou menores a 20')

print(f'D) {homen_mulher[0] + homen_mulher[1]} pessoas participaram dessa pesquisa.')