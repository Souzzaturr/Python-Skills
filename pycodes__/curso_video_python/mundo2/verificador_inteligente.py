ano = input('Digite o ano que você nasceu. ').strip()

while not ano.isnumeric() or int(ano) > 2025 or int(ano) < 1900:
    ano = input('\033[31mDigite apenas números, por favor!\033[m ')

ano = int(ano)

print(f'Você nasceu no ano de \033[33m{ano}\033[m, você tem \033[33m{2025 - ano}\033[m anos!!')