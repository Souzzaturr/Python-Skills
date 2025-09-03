#funções

def area (largura: float, comprimento: float) -> float:
  '''
  Recebe 2 números inteiros e multiplica, retornando uma área;
  Largura: Recebe valor inteiro representando a largura do terreno;
  Comprimento: Recebe valor inteiro representando o comprimento do terreno;
  Retorna -> produto entre largura e comprimento. 
  '''
  return largura * comprimento

def bloco (menssagem: str) -> str:
  """
  Recebe um texto de uma linha, e o envolve por um retangulo de traçinhos '-';
  menssagem: Recebe uma string de até uma linha;
  Retorna -> um bloco com a menssagem dentro."""
  print("+----" + "-" * len(menssagem) + "----+")
  print(f"|    {menssagem}    |")
  print("+----" + "-" * len(menssagem) + "----+")
  return

#programa principal

print(help(area))

print(help(bloco))

bloco("Controle de terrenos")

largura = int(input("Largura (em metros): "))
comprimento = int(input("Comprimento (em metros): "))

print(f"A área desse terreno é: {area(largura, comprimento)}")