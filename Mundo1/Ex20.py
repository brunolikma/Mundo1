from random import shuffle
n1 = str(input("Digite o Primeiro Nome: "))
n2 = str(input("Digite o Segundo Nome: "))
n3 = str(input("Digite o Terceiro Nome: "))
n4 = str(input("Digite o Quarto Nome: "))

lista = [n1, n2, n3, n4]

shuffle(lista)

print("A ordem de apresentação sera: ")
print(lista)