from math import sin, cos, radians, tan

angulo = float(input("Digite o angulo que deseja: "))
seno = sin(radians(angulo))
print(f"O angulo de {angulo} tem o Seno de {seno:.2f}. ")
cosseno = cos(radians(angulo))
print(f"O angulo de {angulo} tem o Cosseno de {cosseno:.2f}")
tangente = tan(radians(angulo))
print(f"O angulo de {angulo} tem a Tangente de {tangente:.2f}")


