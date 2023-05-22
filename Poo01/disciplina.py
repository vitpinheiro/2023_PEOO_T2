#
#entidade:disciplina
#dados necessários:nome da disciplina, notas de 4 bimestres, nota prova final,
#operações: media parcial(com notas bimestrais), media final(todas, caso tenha ficado em prova final)
#considerações: média de aprovação=60, notas de 0 a 100, media parcial ponderada com pesos 2,2,3 e 3, média final=media parcial+nota prova final/2


class Disciplina:
  def __init__(self):
    self.nome = ''
    self.nota1 = 0
    self.nota2 = 0
    self.nota3 = 0
    self.nota4 = 0
    self.provaFinal = 0
  def calc_mediaParcial(self):    
    return ((self.nota1 * 2) + (self.nota2 * 2) + (self.nota3 * 3) + (self.nota4 * 3))/10
  def calc_mediaFinal(self):
    return (self.calc_mediaParcial() + self.provaFinal)/2

x = Disciplina()

print('Digite o nome da disciplina:')
x.nome = input()
print('Digite a nota do primeiro bimestre:')
x.nota1 = int(input())
print('Digite a nota do segundo bimestre:')
x.nota2 = int(input())
print('Digite a nota do terceiro bimestre:')
x.nota3 = int(input())
print('Digite a nota do quarto bimestre:')
x.nota4 = int(input())

print("Media parcial = ", x.calc_mediaParcial())

if x.calc_mediaParcial() < 60:
  print('Digite a nota da prova final:')
  x.provaFinal = int(input())
  print('Média Final = ', x.calc_mediaFinal())