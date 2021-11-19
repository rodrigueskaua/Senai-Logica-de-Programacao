"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que
a porcentagem do distribuidor seja de 28% e os impostos de 45%, escreva um programa
em Python que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

"""

custo_fabrica = float(input("Digite o custo de fábrica do carro: R$"))
custo_do_consumidor = custo_fabrica + (custo_fabrica * 0.28) + (custo_fabrica * 0.45)
print(f"O custo ao consumidor do carro será de: R${custo_do_consumidor:.2f}")