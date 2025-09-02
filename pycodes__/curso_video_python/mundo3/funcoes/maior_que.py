#importações
import random

#funções
def maior_que (*num) -> int:
  maior = num[0]
  for numero in num[1:]:
    if numero > maior:
      maior = numero
  return maior

def line () -> str:
  print("-"*50)
  return

#programa principal
line()
for i in range(5):
  num1 = random.randint(0, 10)
  num2 = random.randint(0, 10)
  num3 = random.randint(0, 10)
  num4 = random.randint(0, 10)
  num5 = random.randint(0, 10)

  print(f"Números escolhidos: {num1}, {num2}, {num3}, {num4}, {num5}")

  print(f"O maior número entre esses números é: {maior_que(num1, num2, num3, num4, num5)}")

  line()