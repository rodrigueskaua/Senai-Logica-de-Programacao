"""
Escreva uma função que receba dois números e retorne verdadeiro (1) ou falso (0) indicando se o primeiro número
é divisível pelo segundo.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

def divisivel(num1, num2):
    if num1 % num2 == 0:
        return 1
    else: return 0

print(divisivel(num1, num2))
