h1, m1 = map(int, input('Digite o primeiro horário no formato hh:mm \n').split(':'))
h2, m2 = map(int, input('Digite o segundo horário no formato hh:mm \n').split(':'))

sumM = m1 + m2
sumH = h1 + h2

if sumM >= 60:
  sumM -= 60
  sumH += 1

sumM = str(sumM)

if len(sumM) == 1:
  sumM = '0' + sumM
print(f'Total de horas = {sumH}:{sumM}')  
