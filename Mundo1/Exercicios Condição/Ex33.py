n1 = int(input("Digite o Primeiro Numero: "))
n2 = int(input("Digite o Segundo Numero: "))
n3 = int(input("Digite o Terceiro Numero: "))
lista = [n1, n2, n3]
ordemLista = sorted(lista)
print(f"O maior numero é {ordemLista[2]} e o menor numero é {ordemLista[0]}")
