"""

17. Escreva um programa em Python que calcule o valor do desconto de uma mercadoria
paga a vista e o valor total a ser pago. O programa deve ler o valor da mercadoria e a
porcentagem do desconto. Depois o programa deve calcular e imprimir na tela o valor do
desconto e o novo valor da mercadoria com o desconto.
"""

valor_mercadoria = float(input("Digite o valor da mercadoria: R$"))
desconto_porcentagem = float(input("Digite a porcentagem para o desconto (%): "))
valor_total = valor_mercadoria - (valor_mercadoria *(desconto_porcentagem / 100))


print(f"O valor de R${valor_mercadoria:.2f} com {desconto_porcentagem}% de desconto é igual a R${valor_total:.2f}.")