class Conta_corrente:
  def __init__ (self, cliente, saldo = 0, deve = 0):
    self.__cliente = cliente
    self.__saldo = saldo if saldo >= 0 else 0
    self.__deve = deve

  def creditar (self, valor):
    self.saldo = self.saldo + valor
    return None

  def debitar (self, valor):
    if self.saldo >= valor:
      self.saldo = self.saldo - valor
    else:
      self.deve += valor - self.saldo
      self.saldo = 0
    return None

  def transferir (self, valor, outra_conta):
    if self.saldo >= valor:
      self.debitar(valor)
      outra_conta.creditar(valor)
    else:
      print("Erro, saldo insuficiente!!")
    return None

  @property
  def cliente (self):
    return self.__cliente

  @property
  def saldo (self):
    return self.__saldo

  @property
  def deve (self):
    return self.__deve

  @saldo.setter
  def saldo (self, valor):
    self.__saldo = valor
    return None

  @deve.setter
  def deve (self, valor):
    self.__deve = valor
    return None

  def __str__ (self):
    return f"{self.cliente} \nSaldo: {self.saldo} \nDeve: {self.deve}"