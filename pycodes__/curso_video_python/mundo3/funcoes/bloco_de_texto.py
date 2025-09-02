#funções
def bloco_menssagem (menssagem: str) -> str:
  print("~" * (8 + len(menssagem)))
  print(f"    {menssagem}    ")
  print("~" * (8 + len(menssagem)))
  return

#programa principal

bloco_menssagem("Teste de bloco")
bloco_menssagem("Muito bom")