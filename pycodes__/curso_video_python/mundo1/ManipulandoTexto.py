#nome = str(input('Whats your name?\n')).strip().title()

#print(f'No nome "{nome}", a letra "A" aparece {nome.upper().replace('Á','A').replace('À','A').count('A')} vezes')
#print(f'No nome "{nome}", a letra "A" aparece pela primeira vez na posição nº{nome.lower().replace(' ','').replace('á','a').replace('à','a').find('a') + 1}')
#print(f'No nome "{nome}", a letra "A" aparece pela ultima vez na posição nº{nome.lower().replace(' ','').replace('á','a').replace('à','a').rfind('a') + 1}')

nome = str(input('Qual o seu nome completo??\n')).strip().title()
lista_nome = nome.split()

print(f'Bem vindo(a), {nome}')
print(f'Seu primeiro nome é {lista_nome[0]}')
print(f'Seu ultimo nome é {lista_nome[len(lista_nome)-1]}')
