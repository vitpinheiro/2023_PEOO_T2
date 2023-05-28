import math

class circulo:
  def __init__(self):
    self.__r=0
  def set_raio(self,v):
    if v>=0: self.__r=v
    else: raise ValueError()
  def get_raio(self):
    return self.__r
  def calc_area(self):
    return math.pi*(self.r**2)
  def calc_circunferencia(self):
    return (2*math.pi)*self.r

class UI:
 @staticmethod
 def main():
   a= circulo()
# c= circulo()
   print("Digite o valor do raio")
   a.r=float(input())
   a.set_raio(a.r)
   print(f"O cálculo da área do círculo é:{a.calc_area()}")

# print("Digite o valor do raio")
# c.r=float(input())
   print(f"O cálculo da circunferência:{a.calc_circunferencia()}") 
UI.main()