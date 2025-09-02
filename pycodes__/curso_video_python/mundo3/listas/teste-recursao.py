def soma_fatorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        return x + soma_fatorial(x - 1)

print("Resultado: " + str(soma_fatorial(1000000)))