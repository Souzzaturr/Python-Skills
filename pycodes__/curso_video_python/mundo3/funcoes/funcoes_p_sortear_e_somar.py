#importações
import random

#funções
def eh_par (num: int) -> bool:
  return num % 2 == 0

def sortear_cinco_numeros (lista_numeros: list) -> list:
  lista_cinco_numeros = list()
  for i in range(5):
    lista_cinco_numeros.append(lista_numeros.pop(random.randint(0, len(lista_numeros) - 1)))
  return lista_cinco_numeros

def soma_valores_pares (lista_numeros: list) -> list:
  soma_pares = 0
  for numero in lista_numeros:
    if eh_par(numero):
      soma_pares += numero
  return soma_pares

def criar_lista_aleatoria () -> list:
  lista_numeros = list()
  for i in range(random.randint(5, 20)):
    lista_numeros.append(random.randint(0, 10))
  return lista_numeros

#codigo principal
lista_num = criar_lista_aleatoria()

print(f"Os números escolhidos foram: {lista_num}")

num_sorteados = sortear_cinco_numeros(lista_num)

print(f"Sorteando 5 dos números mostrados acima, temos: {num_sorteados}")

print(f"A soma dos valores pares entre os 5 valores sorteados acima, é: {soma_valores_pares(num_sorteados)}")