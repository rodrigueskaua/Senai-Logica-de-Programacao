"""Escreva um programa que tenha a variável salario = 1100.00. Peça para o usuário informar os valores das contas de água, luz e internet. Subtraia os valores das contas no salário e exiba qual é o dinheiro restante. """

salario = 1100.00
agua = float(input('Digite o valor da conta de água: R$'))
luz = float(input('Digite o valor da conta de luz: R$'))
internet = float(input('Digite o valor da conta de internet: R$'))

resultado = salario - (agua + luz + internet)
print(f'O valor total do salário é de R${salario}, com os valores das contas descontadas o restante do salário é de R${resultado:.2f}')
