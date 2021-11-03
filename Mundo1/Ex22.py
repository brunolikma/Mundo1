from time import sleep
nome = input("Digite seu nome Completo: ")
print ("Analisando seu nome...")
sleep(3)
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome)} letras")
print(f"Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras.  ")

