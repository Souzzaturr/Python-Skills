frase_original = input('Digite uma frase qualquer.\n').strip()

frase = frase_original.lower().replace(' ', '')

frase_reverse = ''

qtd_letras_in_frase = len(frase)

for i in range(qtd_letras_in_frase - 1, -1, -1):
    
    frase_reverse = frase_reverse + frase[i]

if frase_reverse == frase:
    print(f'A frase "{frase_original}" é um palindromo')
    print(f'Frase na ordem normal: {frase}')
    print(f'Frase na ordem inversa: {frase_reverse}')

else:
    print(f'A frase {frase_original} NÃO é um palindromo')
    print(f'Frase na ordem normal: {frase}')
    print(f'Frase na ordem inversa: {frase_reverse}')
