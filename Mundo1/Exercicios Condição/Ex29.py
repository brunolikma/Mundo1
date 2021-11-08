n1 = int(input("Qual a velocidade atual do carro? "))
if n1 <= 80:
    print("Tenha um bom dia ! Dirija com segurança! ")
else:
    multa = float(n1 - 80) * 7
    print("Multado! Você excedeu o limite permitido que é 80Km/h")
    print(f"Você deve pagar uma multa de R${multa:.2f}! ")
    print("Tenha um bom dia ! Dirija com segurança! ")