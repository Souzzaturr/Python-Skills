class No:
    def __init__ (self, conteudo, proximo = None):
        self.__conteudo = conteudo
        self.__proximo = proximo

    
    @property
    def conteudo (self):
        return self.__conteudo
    
    @property
    def proximo (self):
        return self.__proximo
    
    @proximo.setter
    def proximo (self, ponteiro_proximo):
        self.__proximo = ponteiro_proximo
        return None