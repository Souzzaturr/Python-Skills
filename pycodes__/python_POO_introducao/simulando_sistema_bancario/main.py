from banco_class import Banco
from conta_corrente_class import Conta_corrente
from cliente_class import Cliente


arturo_bank = Banco("Arturo Bank")


artur_cliente = Cliente("Artur", 78965432112)

artur_account = Conta_corrente(artur_cliente, -1, 0)

print(artur_account)


thiago_cliente = Cliente("Thiago", 4569812312)

thiago_account = Conta_corrente(thiago_cliente, 90, 0)

print(thiago_account)


artur_account.creditar(150)

thiago_account.debitar(30)


print(artur_account)
print(thiago_account)


artur_account.transferir(4000, thiago_account)


arturo_bank.adiciona_conta(artur_account)
arturo_bank.adiciona_conta(thiago_account)


for i in range(len(arturo_bank.contas)):
  print(arturo_bank.contas[i])