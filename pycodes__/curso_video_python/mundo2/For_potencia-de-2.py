while True:
    num = int(input('Digite quantos dígitos de potência de dois você quer.\n'))

    if num < 1:
        break

    for i in range(num):
        print(f'2^{i} = {2**i}')

    print(f'2^{num} = {2**num}')
        

print('FIM')
