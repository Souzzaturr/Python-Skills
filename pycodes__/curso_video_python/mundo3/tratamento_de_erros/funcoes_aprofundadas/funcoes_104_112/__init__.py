#Funções (Refazendo o tratamento das funções dos exercícios 104 e 112)
def validador_entrada (menssagem = "Digite um número inteiro qualquer: ") -> int:
    """Recebe -> uma menssagem, que será exibida para o usuario.
    A função irá pedir um numero inteiro válido até que o usuario digite um;
    Retorna -> Um número inteiro."""
    
    while True:
        try:
            num = int(input(menssagem).replace(" ", ""))
        
        except ValueError:
            print(f"\033[1;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!!\033[m")

        except KeyboardInterrupt:
            print(f"\n\033[1;31mUsuario preferiu não digitar esse número.\033[m")

            return 0
        
        else:
            break

    return num



def eh_float (menssagem: str) -> float:
    """Recebe -> uma menssagem, que será exibida para o usuario;
    A função irá pedir um numero real válido até que o usuario digite um;
    Retorna -> Um número real (um float)."""

    while True:
        try:
            num = float(input(menssagem).replace(" ", "").replace(",", "."))
        
        except ValueError:
            print(f"\033[1;31mERRO! DIGITE UM NÚMERO REAL VÁLIDO!!\033[m")
        
        except KeyboardInterrupt:
            print(f"\n\033[1;31mUsuario preferiu não digitar esse número.\033[m")
            
            return 0
        
        else:
            break

    return num