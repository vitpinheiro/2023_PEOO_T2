# 4. Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores podem ser números reais. Mostrar o resultado com duas casas decimais.

b=float(input("Digite a base \n"))
h=float(input("Digite a altura \n"))

a=b*h
p=2*(a+b)
d=(a**2+b**2)**0.5

print("O valor da área é: {:.2f}".format(a))
print("O valor do perímetro é: {:.2f}".format(p))
print("O valor da diagonal é: {:.2f}".format(d))
