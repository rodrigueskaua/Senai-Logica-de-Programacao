"""24. Um sistema de máquinas demora 37 segundos para produzir uma peça. Sua tarefa é
fazer um programa em Python que leia a quantidade de peças a ser produzida e calcule o
tempo em horas, minutos e segundos necessário para produzir essa quantidade de peças.
Exemplo: Se digitado pelo usuário a quantidade 250, deverá aparecer na tela 2 horas, 34
minutos e 10 segundos.
"""

quantidades_de_peças = int(input("Digite a quantidade de peças a ser produzidas: "))
tempo_de_produção = quantidades_de_peças * 37
horas = tempo_de_produção / 60
print(f"""Hora(s):
Minuto(s):
Segundo(s):""")