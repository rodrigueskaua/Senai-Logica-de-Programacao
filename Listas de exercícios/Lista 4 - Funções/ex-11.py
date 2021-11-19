"""
11. Escreva um programa em Python que leia os valores da base maior (B), base menor
(b) e altura (h) de um trapézio e calcule e imprima o valor de sua área, sabendo que a área
de um trapézio (A) é dada 
"""



base_maior = float(input("Digite a base maior do trapésio (B): "))
base_menor = float(input("Digite a base menor do trapésio (b): "))
altura = float(input("Digite a altura do trapésio (A): "))
area = (base_maior + base_menor) * altura / 2
print(f"O valor da área desse trapésio é {area:.2f}")