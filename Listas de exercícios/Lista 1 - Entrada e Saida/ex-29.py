"""
Escreva um programa em Python que, dadas as dimensões das figuras apresentadas
(lidas do teclado) calcule o volume e a área da Superfície de cada um. Primeiro o usuário
vai entrar com os lados do paralelepípedo, então programa já pode mostrar o volume e a
área desta figura. Depois entra com a área da base e altura do cilindro, obtendo a resposta
e por fim entra com o raio da esfera e o programa faz o último cálculo.
"""

print("Digite as informações do paralelepípedo: ")
a_parale= float(input("Digite o lado (a) do paralelepípedo: "))
b_parale = float(input("Digite o lado (b) do paralelepípedo: "))
c_parale = float(input("Digite o lado (c) do paralelepípedo: "))
volume_parale = a_parale * b_parale * c_parale
area_sup_parale = 2 * ((a_parale * b_parale) + (b_parale * c_parale) + (c_parale * a_parale))

print(f"""\nVolume e Área da Superfície desse Paralelepípedo:
Volume = {volume_parale:.2f}
Área da Superfície = {area_sup_parale:.2f} \n""")


print("Digite as informações do Cilindro: ")
ab_cilindro= float(input("Digite a área da base do Cilindro (Ab): "))
al_cilindro = float(input("Digite a lateral do Cilindro (Al): "))
h_cilindro = float(input("Digite a altura do Cilindro (h): "))
volume_cilindro = ab_cilindro * h_cilindro
area_sup_cilindro = ab_cilindro + al_cilindro

print(f"""\nVolume e Área da Superfície desse Cilindro:
Volume = {volume_cilindro:.2f}
Área da Superfície = {area_sup_cilindro:.2f}\n""")


print(f"""\nVolume e Área da Superfície desse Paralelepípedo:
Volume = {volume_parale:.2f}
Área da Superfície = {area_sup_parale:.2f} \n""")


print("Digite as informações da esfera: ")
raio_esfera= float(input("Digite o raio da esfera (R): "))

volume_raio = 4 * 3.14159265359 * raio_esfera ** 3 / 3
area_sup_raio = 4 * 3.14159265359 * raio_esfera ** 2

print(f"""\nVolume e Área da Superfície dessa esfera:
Volume = {volume_raio:.2f}
Área da Superfície = {area_sup_raio:.2f}""")