n1 = int(input("Digite o primerio valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o Terceiro valor: "))
lista = [n1, n2, n3]
listaOrdenada = sorted(lista)

if listaOrdenada[2] < listaOrdenada[0] + listaOrdenada[1]:
    print("Da para fazer um triangulo")
else:
    print("Não da para fazer um triangulo")
