"""
25. Faça um programa em Python que solicite ao usuário a nota de suas 3 provas e
imprima a média aritmética delas.
"""

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3 

print(f"A média aritmética das provas é: {media:.2f}")
