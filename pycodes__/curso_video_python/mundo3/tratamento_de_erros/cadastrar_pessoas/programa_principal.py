from funcoes_115 import dado, numeros, visual


while True:
    #Exibe um bloco 'menu inicial'
    print(visual.bloco(f"\033[1;36mMENU INICIAL\033[m"))

    #Exibe menu com 3 opções
    visual.opcoes()

    #Recebe opção escolhida pelo usuario
    while True:
        try:
            acao = int(input(f"\033[1;33mDigite sua opção:\033[m "))
        
        except ValueError:
            print(f"\033[1;31mDigite apenas números!!\033[m")
        
        else:
            if acao >= 1 and acao <= 3:
                break
            
            else:
                print(f"\033[1;31mDigite uma opção entre as três acima!!\033[m")
    
    #Opção 1 - (Exibir pessoas já cadastradas)
    if acao == 1:
        print(visual.bloco("PESSOAS CADASTRADAS"))

        print(visual.exibir_pessoas())
    
    else:
        #Opção 2 - (Realizar um cadastro de uma nova pessoa)
        if acao == 2:
            print(visual.bloco("NOVO CADASTRO"))

            #Recebe o nome
            while True:
                nome = input("Nome: ")

                if len(nome) > 0:
                    break

                else:
                    print(f"\033[1;31mDigite um nome válido!!\033[m")


            #recebe a idade
            while True:
                try:
                    idade = int(input("Idade: "))
                
                except ValueError:
                    print(f"\033[1;31mDigite apenas números!!\033[m")
                
                else:
                    if numeros.idade_valida(idade):
                        break

                    else:
                        print(f"\033[1;31mDigite uma idade válida\033[m")
            
            #Guarda o nome e a idade no banco de dados
            dado.guardar_cadastro(nome, idade)

            print(f"\033[1;32m{nome.split()[0]} Cadastrado com sucesso!!\033[m")

        #Opção 3 (Sair do programa)
        else:
            print(f"\033[1;33m----FINALIZANDO PROGRAMA----\033[m")
            break