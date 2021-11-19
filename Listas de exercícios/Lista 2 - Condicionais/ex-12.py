"""
12. Escreva um programa em Python que leia o peso e a altura de uma pessoa. Em
seguida o programa deve calcular e imprimir índice de massa corpórea (IMC) dessa
pessoa. Dado:
𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 / 𝑎𝑙𝑡𝑢𝑟𝑎²
"""

peso = float(input("Digite o peso (Kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / altura ** 2 

print(f"O índice de massa corpórea (IMC) é: {imc:.2f}")