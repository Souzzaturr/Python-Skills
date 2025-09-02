print(f'{'SISTEMA ESCOLAR':=^50}')
print()

lista_alunos = list()

while True:
    nome = input('Digite o nome de um aluno: ')

    if nome == '':
        print('FINALIZANDO LEITURA...')
        break

    nota1 = float(input(f'Digite a 1ª nota de {nome}: '))
    nota2 = float(input(f'Digite a 2ª nota de {nome}: '))

    aluno = nome, nota1, nota2
    lista_alunos.append(aluno)

    print()
    print(f'Informações de {nome} salvas com sucesso!!')
    print('-' * 50, end='\n\n')

print(f'{'Nº    NOME          MÉDIA': ^50}')
print('-' * 50)

for aluno in lista_alunos:
    print(' ' * 11, lista_alunos.index(aluno), ' ' * 3, aluno[0], ' ' * (13 - len(aluno[0])), (aluno[1] + aluno[2])/2)

while True:
    print('-' * 50, end='\n\n')

    nota_aluno = input('Deseja ver cada nota de algum aluno? digite o nome dele aqui: ')

    if nota_aluno == '':
        print('PROGRAMA FINALIZADO')
        break

    for aluno in lista_alunos:
        if nota_aluno == aluno[0]:
            print(f'As notas de {aluno[0]} são: {aluno[1]} e {aluno[2]}.')
            break