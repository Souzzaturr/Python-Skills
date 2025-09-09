try:
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite um número inteiro: "))

except Exception as erro:
    print("São permitidos apenas números inteiros!!")
    print(f"Código do erro: {erro.__class__}")

else:
    try:
        c = a / b
        print(f"Divisão de {a} por {b} = {c}")
        print("Só sucesso")

        print("Resto do código...")

        print("...")
    
    except Exception as erro:
        print("Não é possível realizar operação -> Divisão por zero!!")
        print(f"Código do erro: {erro.__class__}")
        

finally:
    print("--FIM DO PROGRAMA--")