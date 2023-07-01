class Jogador:
  def __init__(self, nome, gols):
    self.__nome = nome
    self.__gols = gols
  def get_gols(self):
    return self.__gols
  def __str__(self):
    return f"{self.__nome} - {self.__gols} gol(s)"

class Time:
  def __init__(self, nome):
    self.__nome = nome
    self.__jogadores = []
  def inserir(self, j):
    self.__jogadores.append(j)
  def listar(self):
    return self.__jogadores
  def artilheiro(self):
    if len(self.__jogadores) == 0: return None
    art = self.__jogadores[0] 
    for j in self.__jogadores:
      if j.get_gols() > art.get_gols():
        art = j
      return art  

class UI:
  @staticmethod
  def menu():
    print("0-Fim, 1-Inserir, 2-Listar, 3-Artilheiro")
    return int(input())

  @staticmethod
  def main():
    op = 10
    x = Time("IFRN")    
    while op != 0:
      op = UI.menu()
      if op == 1:
        nome = input("Nome do jogador: ")
        gols = int(input("Gols: "))
        j = Jogador(nome, gols)
        x.inserir(j)
      if op == 2:  
        for j in x.listar(): print(j)
      if op == 3:  
        print(x.artilheiro())

UI.main()