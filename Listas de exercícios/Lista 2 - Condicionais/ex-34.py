"""
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.
"""
print('Digite o valor do salário atual para calcularmos o valor do seu aumento:')
salario = float(input('R$ '))

if salario > 1250.00:
    aumento = salario + (salario * 0.10)
    print(f'O valor do seu novo salário é de R${aumento:.2f}')
else: 
    aumento = salario + (salario * 0.15)
    print(f'O valor do seu novo salário é de R${aumento:.2f}')