class Pilha:
    def __init__ (self, proximo = None):
        self.__proximo = proximo   

    @property
    def topo (self):
        return self.__proximo    

    
    def tah_vazio (self):
        return self.__proximo == None   


    def empilhar (self, no):
        if self.tah_vazio():
            self.__proximo = no
        
        else:
            no.proximo = self.__proximo
            self.__proximo = no
        
        return None    


    def desempilhar (self):
        if self.tah_vazio():
            return None

        topo = self.topo
        self.__proximo = self.topo.proximo
        return topo
    

    def __str__ (self):
        ponteiro = self.topo
        conteudo = ""
        
        while ponteiro != None:
            conteudo += f"{ponteiro}, "
            ponteiro = ponteiro.proximo
        
        return conteudo