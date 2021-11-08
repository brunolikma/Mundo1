nome = str(input("Digite seu Nome completo: ")).strip()
nomeSeparado = nome.split()
print(f"Seu primeiro nome é: {nomeSeparado[0]} ")
print(f"Seu ultimo nome é: {nomeSeparado[len(nomeSeparado)-1]}")
