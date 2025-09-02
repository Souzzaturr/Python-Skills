palavra = input()

for letra in palavra:
    print(letra, end=' -> ')
    if ord(letra) >= 65 and ord(letra) <= 90:
        print('Maiúscula')
    else:
        if ord(letra) >= 97 and ord(letra) <= 122:
            print('Minúscula')
        else:
            if ord(letra) >= 48 and ord(letra) <= 57:
                print('Número')
            else:
                print('Caractere especial')
