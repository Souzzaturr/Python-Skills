class Fila:
    def __init__ (self, inicio = None):
        self.__inicio = inicio

    
    @property
    def exibir_inicio (self):
        if self.tah_vazio:
            return ""
        
        return self.__inicio.conteudo
    

    @property
    def exibir_fim (self):
        if self.tah_vazio:
            return ""
        
        ponteiro = self.__inicio

        while ponteiro.proximo != None:
            ponteiro = ponteiro.proximo

        return ponteiro.conteudo
    

    @property
    def tah_vazio (self):
        return self.__inicio == None
    

    @property
    def tamanho (self):
        tamanho = 0
        ponteiro = self.__inicio

        while ponteiro != None:
            tamanho += 1
            ponteiro = ponteiro.proximo

        return tamanho
    

    def adiciona (self, novo_no):
        if self.tah_vazio:
            self.__inicio = novo_no
        
        else:
            novo_no.proximo = self.__inicio
            self.__inicio = novo_no
        
        return None
    

    def remove (self):
        if self.tah_vazio:
            return None
        
        if self.__inicio.proximo == None:
            valor = self.__inicio.conteudo
            self.__inicio = None
            return valor
        
        ponteiro = self.__inicio

        while ponteiro.proximo != None:
            ponteiro_anterior = ponteiro
            ponteiro = ponteiro.proximo

        valor = ponteiro.conteudo
        ponteiro_anterior.proximo = None
        
        return valor
    

    def __str__ (self):
        ponteiro = self.__inicio
        texto = ""

        while ponteiro != None:
            texto += f"{ponteiro.conteudo}, "
            ponteiro = ponteiro.proximo

        return texto