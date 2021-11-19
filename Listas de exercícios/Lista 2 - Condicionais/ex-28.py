"""Escreva um programa em Python que, dados os valores a, b e c de uma equação
quadrática ax²+bx+c = 0, calcule a maior das raízes que resolve a equação. Suponhamos
que o valor calculado para delta é sempre positivo, ou seja, b² > 4ac.
"""

a = float(input("Digite o valor de (a): "))
b = float(input("Digite o valor de (b): "))
c = float(input("Digite o valor de (c): "))

delta = b ** 2 - 4 * a * c
Xi = (-b +  delta ** 0.5)  / (2 * a)
Xii = (-b -  delta ** 0.5)  / (2 * a)
print(f" As raises são {Xi} e {Xii}")