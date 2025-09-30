class Banco:
  def __init__ (self, nome, contas = []):
    self.__nome = nome
    self.__contas = contas

  @property
  def nome (self):
    return self.__nome

  @property
  def contas (self):
    return self.__contas

  @contas.setter
  def contas (self, lista):
    self.__contas = lista
    return None

  def somar_saldos (self):
    soma = 0
    for i in range(len(self.contas)):
      soma = self.contas.saldo
    return soma

  def adiciona_conta (self, conta):
    if not conta in self.contas:
      self.contas.append(conta)
    return None

  def remove_conta (self, conta):
    self.contas.remove(conta)
    return None