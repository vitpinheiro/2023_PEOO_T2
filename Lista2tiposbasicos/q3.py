# 3. Calcular a média parcial de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres (pesos 2 e 3). Considerar as notas com valores inteiros entre zero e cem.

n1=int(input("Digite a sua primeira nota \n"))
n2=int(input("Digite a sua segunda nota \n"))

if n1>=0 and n2>=0 and n1<=100 and n2<=100:
  mp=(n1*2)+(n2*3)/5
  print(f"Média parcial={mp}")
else:
  print("As notas não estão entre zero e cem")
  
