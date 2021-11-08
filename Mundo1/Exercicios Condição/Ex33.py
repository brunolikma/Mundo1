n1 = int(input("Digite o Primeiro Numero: "))
n2 = int(input("Digite o Segundo Numero: "))
n3 = int(input("Digite o Terceiro Numero: "))
lista = [n1, n2, n3]
decrecenteLista = sorted(lista,reverse=True)
print(f"O maior numero é {decrecenteLista[0]} e o menor numero é {decrecenteLista[len(decrecenteLista) - 1]}")
