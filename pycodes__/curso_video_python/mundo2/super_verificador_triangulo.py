def eh_triangulo(x: int, y: int, z: int) -> bool:
    return x + y > z and x + z > y and y + z > x

def tipo_triangulo(x: int, y: int, z: int) -> str:
    tipo = str()
    if x == y and x == z:
        tipo = 'Equilátero'
    else:
        if x == y or x == z or y == z:
            tipo = 'Isóceles'

        else:
            tipo = 'Escaleno'
    return tipo

while True:
    print('Digite "S" para confirmar que quer testar se determinadas retas formam um triângulo.')
    print('Digite "X" se quiser encerrar o programa.')
    resposta = input()

    if resposta == 'x' or resposta == 'X':
        print('PROGRAMA ENCERRADO')
        break

    else:
        print('Vamos começar!!')

    lista_retas = [0, 0, 0]

    for i in range(3):
        lista_retas[i] = int(input('Digite abaixo o comprimento de uma reta qualquer.\n'))

    if not eh_triangulo(lista_retas[0], lista_retas[1], lista_retas[2]):
        print(f'As retas {lista_retas[0]}, {lista_retas[1]}, {lista_retas[2]} NÃO formam triângulo!!\n')

    else:
        print(f'As retas {lista_retas[0]}, {lista_retas[1]}, {lista_retas[2]} formam triângulo!!')

        print(f'A combinação dessas três retas forma um triângulo {tipo_triangulo(lista_retas[0], lista_retas[1], lista_retas[2])}!!\n')
