class Cliente:
  def __init__ (self, nome, cpf):
    self.__nome = nome
    self.__cpf = cpf

  @property
  def cpf (self):
    return self.__cpf

  @property
  def nome (self):
    return self.__nome

  def __str__ (self):
    return f"Nome: {self.nome} \nCPF: {self.cpf}"