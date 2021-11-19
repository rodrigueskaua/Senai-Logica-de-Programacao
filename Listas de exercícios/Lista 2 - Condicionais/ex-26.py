"""
26. Repita o exercício anterior usando apenas duas variáveis.
"""

soma = 0
for i in range(3):
    notas = float(input("Digite a nota da prova: "))
    soma += notas 
print(f"A média aritmética das provas é: {soma / 3:.2f}")
