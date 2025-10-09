#Este arquivo comtém a classe "Nó"

class No:
    def __init__ (self, conteudo, proximo = None):
        self.__conteudo = conteudo
        self.__proximo = proximo
    
    @property
    def proximo (self):
        return self.__proximo

    @proximo.setter
    def proximo (self, ponteiro):
        self.__proximo = ponteiro
        return None
    

    def __str__ (self):
        return f"{self.__conteudo}"