# Leia os quatro valores correspondentes aos eixos x e y de dois pontos do plano, p1 (x1, y1) e p2 (x2, y2) e calcule a distância entre eles, mostrando quatro casas decimais após a vírgula, conforme a fórmula : x2-x1+y2-y1**0.5**2

x1=float(input("Digite quem é o x1 \n"))
y1=float(input("Digite quem é o y1 \n"))
x2=float(input("Digite quem é o x2 \n"))
y2=float(input("Digite quem é o y2 \n"))

d=(x2-x1+y2-y1)**0.5**2

print("Distância = {:.4f}".format(d))
