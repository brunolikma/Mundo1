km = float(input("Digite quantos KM foram percorridos: "))
dias = int(input("Digite quantos dias foram usados o veiculo: "))
diasTotal = dias * 60
kmtotal = km * 0.15
totalPagar = float(diasTotal + kmtotal)

print(f"Voce utilizou o veiculo por {dias} dias e percorreu {km} km o total a pagar é de R${totalPagar:.2f}")