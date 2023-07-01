class Esporte:
  def __init__(self, nome, mensalidade):
    self.__nome = nome
    self.__mensalidade = mensalidade
  def get_mensalidade(self):
    return self.__mensalidade
  def __str__(self):
    return f"Nome: {self.__nome} - valor: {self.__mensalidade} reais "
class Academia:
  def __init__(self, nome):
    self.__nome = nome
    self.__esportes = []
  def inserir(self, e):
    self.__esportes.append(e)
  def listar(self):
    return self.__esportes
  def media(self):
    media = 0
    for esporte in self.__esportes:
      media += esporte.get_mensalidade()
    return media / len(self.__esportes)
  def __str__(self):
    return f"Nome: {self.__nome}- Esportes: {self.__esportes}"


class UI:
  @staticmethod
  def menu():
    print("0-fim, 1-inserir, 2-listar, 3-Média")
    return float(input())

  @staticmethod
  def main():
    op=10
    x= Academia("IFRN")
    while op!= 0:
      op = UI.menu()
      if op == 1:
       nome= input("Nome do esporte:")
       mensalidade= float(input("Mensalidade:"))
       e= Esporte(nome, mensalidade)
       x.inserir(e)
      if op ==2:
        for e in x.listar(): print(e)
      if op ==3:
        print(x.media())


UI.main()
    
 
    
    