#funções

def area (largura: float, comprimento: float) -> float:
  return largura * comprimento

def bloco (menssagem: str) -> str:
  print("+----" + "-" * len(menssagem) + "----+")
  print(f"|    {menssagem}    |")
  print("+----" + "-" * len(menssagem) + "----+")
  return

#programa principal

bloco("Controle de terrenos")

largura = int(input("Largura (em metros): "))
comprimento = int(input("Comprimento (em metros): "))

print(f"A área desse terreno é: {area(largura, comprimento)}")