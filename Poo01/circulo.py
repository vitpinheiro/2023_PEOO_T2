import math

class circulo:
  def __init__(self):
    self.r=0
    
  def calc_area(self):
    return math.pi*(self.r**2)
  def calc_circunferencia(self):
    return (2*math.pi)*self.r


a= circulo()
# c= circulo()
print("Digite o valor do raio")
a.r=float(input())
print(f"O cálculo da área do círculo é:{a.calc_area()}")

# print("Digite o valor do raio")
# c.r=float(input())
print(f"O cálculo da circunferência é:{a.calc_circunferencia()}")