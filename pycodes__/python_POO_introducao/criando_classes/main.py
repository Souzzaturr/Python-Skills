from aluno_class import Aluno
from retangulo_class import Retangulo
from conta_bancaria_class import Conta_bancaria

base_caixote = Retangulo(10, 30)

artur = Aluno("Artur", 202521840200)

thiago_account = Conta_bancaria("Thago José M.", 76497572602, 15469151)


print(base_caixote.h)

print(base_caixote.b)


print(artur.name)

print(artur.matricula)


print(thiago_account.name)

print(thiago_account.cpf)

print(thiago_account.account_number)