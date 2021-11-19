"""
14. Faça um programa em Python que leia uma temperatura fornecida em graus fahrenheit
e a converta para o seu equivalente em graus centígrados, imprimindo este valor na tela.
Dado:
"""

f = float(input("Digite a temperatura em graus fahrenheit: "))
c =  (f - 32) / 1.8
print(f"A temperatura de {f} graus fahrenheit convertida para graus celcius é: {c:.2f}")