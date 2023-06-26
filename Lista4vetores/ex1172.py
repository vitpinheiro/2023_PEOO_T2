class Bingo:
  def __init__(self):
    self.__numBolas=10
    self.__sorteados=[]
  def Iniciar(self, numBolas):
    if numBolas>0:
      self.__numBolas= numBolas
      self.__sorteados= []
    else:
      raise ValueError()
    def proximo(self):
      # testar de todos os números já foram sorteados
    if len(self.__sorteados)==self.__numBolas:
      return -1
     # sortear um número entre 1 e numBolas
     # enquanto não sortear um número novo
      x= random.randrange(1, self.__numBolas + 1)
      while x in self.__sorteados:
        x= random.randrange(1, self.__numBolas + 1)
      self.__sorteados.append(x)
      return x
    def sorteados(self):
      aux = self.__sorteados
      aux.sort()
      return aux

class UI:
  @staticmethod
  def main():
    op = int(input("1 - Novo Jogo, 2 - Sortear, 3 - Sorteados, 0 - Fim: "))
    jogo = Bingo()
    while op != 0:
      if op == 1:
        n = int(input("Quantas bolas no bingo? "))
        jogo.Iniciar(n)
      if op == 2:
        x = jogo.Proximo()
        if x == -1: print("Fim do Jogo")
        else: print(f"Bola sorteada: {x}")  
      if op == 3:
        print(f"Bolas já sorteadas: {jogo.Sorteados()}")
      op = int(input("1 - Novo Jogo, 2 - Sortear, 3 - Sorteados, 0 - Fim: "))

UI.main()