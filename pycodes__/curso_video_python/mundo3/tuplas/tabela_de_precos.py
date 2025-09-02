import random

def criar_string () -> str:
    palavra = str()
    for i in range(random.randint(3, 14)):
        letra = chr(random.randint(97, 122))
        palavra = palavra + letra
    return palavra

#----

produtos = tuple()

for i in range(random.randint(3, 10)):
    produtos = produtos + (criar_string(), float(random.randint(1, 99)))

print('-' * 50)
print(' ' * 16, 'TABELA DE PREÇOS', ' ' * 16)
print('-' * 50)

for i in range(0, len(produtos), 2):
    produto, preco = produtos[i:i+2]
    print(produto, '.' * (41 - len(produto)), 'R$', preco)

print('-' * 50)