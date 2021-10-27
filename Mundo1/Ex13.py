nome = input("Digite seu Nome:")
salario = float(input("Digite seu Salario: "))
salarioAumento = salario + (salario * 0.15)

print(f"Ola {nome} voce teve um rejuste no seu salario antes era {salario:.2f} e com o reajuste \n"
      f" de 15% foi para {salarioAumento:.2f}!!!!!!!!! ")
