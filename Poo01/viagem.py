# A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem realizada. A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de acordo com a distância e o tempo gasto.

class viagem:
  def __init__(self):
    self.distancia=0
    self.horas=0
    self.minutos=0

  def calc_velocidademedia(self):
    return self.distancia/((self.horas*60 + self.minutos)/60)
  
x = viagem()
  
x.distancia= float(input('digite a distância em km \n'))
x.horas= float(input('digite o tempo gasto em horas \n'))
x.minutos= float(input('digite o tempo gasto em minutos \n'))
  
print('A velocidade média é:', x.calc_velocidademedia())
  