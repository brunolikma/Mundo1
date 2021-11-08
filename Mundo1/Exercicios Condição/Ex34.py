salario = float(input("Digite o Salario: "))
if salario > 1250:
    salarioNovo = salario + (salario * 0.10)
else:
    salarioNovo = salario + (salario * 0.15)

print(f"O seu salario era de R${salario:.2f} e foi ajustado para R${salarioNovo:.2f} ")
