"""
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e 
diga ao usuário se elas podem ou não formar um triângulo.
"""

print('-=' * 20)
print("ANALISADOR DE TRINÂNGULOS")
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))


if r1 < r3 + r2 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR trinângulo')
else:
    print('Os segmentos acima NÂO PODEM FORMAR trinângulo')
