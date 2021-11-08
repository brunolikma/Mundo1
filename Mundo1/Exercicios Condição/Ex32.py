from time import sleep

print("=" * 30)
print("SABENDO SE O ANO É BISEXTO")
print("=" * 30)
ano = int(input("Digite um ano qualquer: "))
anoMod4 = ano % 4
anoMod100 = ano % 100
anoMod400 = ano % 400
sleep(2)
if anoMod4 == 0 and anoMod100 != 0 or anoMod400 == 0:
    print("É ano bisexto !!")
else:
    print("Nao é um ano bisexto")