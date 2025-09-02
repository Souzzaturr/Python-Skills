#funções
def contador (*numero) -> int:
  if numero[1].isnumeric() or len(numero[1]) > 1 and numero[1][0] == "-" and numero[1][1:].isnumeric():
    fim = int(numero[1])
  else:
    fim = 10

  if numero[0].isnumeric() or len(numero[0]) > 1 and numero[0][0] == "-" and numero[0][1:].isnumeric():
    inicio = int(numero[0])
  else:
    inicio = 1

  if numero[2].isnumeric() or len(numero[2]) > 1 and numero[2][0] == "-" and numero[2][1:].isnumeric():
    if numero[2] != "0":
      passos = int(numero[2])
    else:
      passos = 1
  else:
    passos = 1

  if inicio > fim and passos > 0:
    passos *= -1
  count = inicio

  while count <= fim if inicio < fim else count >= fim:
    print(count)
    count += passos
  return

#---

def bloco_menssagem (menssagem: str) -> str:
  print("~" * (8 + len(menssagem)))
  print(f"    {menssagem}    ")
  print("~" * (8 + len(menssagem)))
  return

#programa principal
bloco_menssagem("Contador")

inicio = input("INICIO: ")

fim = input("FIM: ")

passos = input("PASSOS: ")

bloco_menssagem("Iniciando contagem...")

contador(inicio, fim, passos)