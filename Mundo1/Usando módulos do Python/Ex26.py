frase = str(input("Digite uma Frase: ")).upper().strip()
letra = "A"
print(f"A letra A aparece {frase.count(letra)} na frase.")
print(f"A primeira letra A aparece na posição {frase.find(letra) + 1 }")
print(f"A ultima letra A aparece na posição {frase.rfind(letra) + 1 }")
