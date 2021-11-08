n1 = float(input(f"Digite a distancia da sua viagem: "))
print(f"Você esta prestes a comecar uma viagem de {n1:.1f}Km.")
if n1 <= 200:
    viagem = n1 * 0.50
else:
    viagem = n1 * 0.45
print(f"E o preço da sua passagem será de R${viagem:.2f}")