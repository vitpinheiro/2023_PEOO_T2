class triangulo:
  def __init__(self,b,h):
    self.__b=0
    self.__h=0
    self.set_base(b)
    self.set_altura(h)
  def set_base(self,v):
    if v>=0:self.__b=v
    else: raise valueError()
  def set_altura(self,v):
    if v>=0:self.__h=v
    else: raise ValueError()
  def get_base(self):
    return self.__b
  def get_altura(self):
    return self.__h
  def calc_area(self):
    return self.__b * self.__h / 2
  def __str__(self):
    return f"Base = {self.__b} - Altura = {self.__h}"

class UI:
  @staticmethod
  def main():
    b=float(input("Digite o valor da base \n"))
    h=float(input("Digite o valor da altura \n"))
    x=triangulo(b,h)
    """print("Digite o valor da base")
    x.b=float(input())
    x.set_base(x.b)
    print("Digite o valor da altura")
    x.h=float(input())
    x.set_altura(x.h)"""
    print(x)
    print(f"A área do triângulo é: {x.calc_area()}")
   
   
UI.main()