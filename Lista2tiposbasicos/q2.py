# 2. Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao Python, <xxx>”, onde <xxx> é o primeiro nome da pessoa.
n=input("Digite o seu nome completo \n")
nome=n.split()
print("Bem vindo ao Python, {}".format(nome[0]))
