# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2 metros quadrados.

n1 = float(input("Digite a Largura da parede: "))
n2 = float(input("Digite a Altura da parede: "))
metrosQuadrados = n1 * n2
tintaPinta = 2 ** 2
latasUsadas = metrosQuadrados / tintaPinta
arrendondaTinta = int(latasUsadas + 1)

print (f"A Largura {n1:.2f} e a Altura {n2:.2f} equivalem a  {metrosQuadrados:.2f} Metros quadrados")

if metrosQuadrados % tintaPinta != 0:
    print(f"{arrendondaTinta} São necessarias para para pintar a parede !")
else:
    print(f"{int(latasUsadas)} São necessarias para para pintar a parede !!")
