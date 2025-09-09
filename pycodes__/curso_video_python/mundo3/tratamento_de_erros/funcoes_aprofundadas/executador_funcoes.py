#Importações
from funcoes_104_112 import validador_entrada, eh_float

#Programa Principal
num_int = validador_entrada("Digite um número Inteiro ")
num_float = eh_float("Digite um número Real ")

print(f"\nOs números digitados foram: \033[1;33m{num_int}\033[m e \033[1;33m{num_float}\033[m")