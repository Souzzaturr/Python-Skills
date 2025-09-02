nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

media_aritmetica = (nota1 + nota2 + nota3) / 3
media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

media_final = media_aritmetica / media_ponderada

print('Notas: ', nota1, nota2, nota3)
print('Média aritmética: ', media_aritmetica)
print(f'Média ponderada: {media_ponderada}')
print(f'Média final = {media_final}')
