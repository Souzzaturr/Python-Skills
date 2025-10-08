#Criando a classe No

class No:
    def __init__ (self, dado, proximo = None):
        self.__dado = dado
        self.__proximo = proximo
    
    def encadear (self, ponteiro):
        temp = self

        while temp.__proximo != None:
            temp = temp.__proximo

        temp.__proximo = ponteiro

        return None
    
    def desencadear (self):
        temp = self

        while temp.__proximo.__proximo != None:
            temp = temp.__proximo
        
        temp.__proximo = None
        return None
    
    def listar_nos (self):
        lista_str = ""

        temp = self

        while temp != None:
            lista_str += f"{temp}, "

            temp = temp.__proximo
        
        return lista_str
    
    def __str__ (self):
        return f"{self.__dado}"
    

#programa principal

print("--- Lista Encadeada (com classe) ---", end = "\n\n")

inicio_lista = No(int(input("Digite um número qualquer: \n")))

while True:
    try:
        no = No(int(input("Digite mais um número (ou qualquer outra coisa para parar) \n")))
    
    except:
        break

    else:
        inicio_lista.encadear(no)

print("Os números digitados foram:")

temp = inicio_lista

print(inicio_lista.listar_nos())

print()