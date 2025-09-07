try:
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite um número inteiro: "))

    try:
        c = a / b
        print(f"Divisão de {a} por {b} = {c}")
    
    except Exception as erro:
        print("Não é possível realizar operação -> Divisão por zero!!")
        print(f"Código do erro: {erro.__class__}")

except Exception as erro:
    print("São permitidos apenas números inteiros!!")
    print(f"Código do erro: {erro.__class__}")

else:
    print("Só sucesso")

    print("Resto do código...")

    print("...")

finally:
    print("--FIM DO PROGRAMA--")