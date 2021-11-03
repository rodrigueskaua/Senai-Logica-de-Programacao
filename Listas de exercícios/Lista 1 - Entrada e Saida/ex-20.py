"""
Um fabricante paga uma porcentagem de imposto sobre o total de uma venda
realizada. Esse fabricante conhece a quantidade de unidades de um produto que produziu
e o valor de cada peça. Ajude este fabricante escrevendo um programa em Python que
permita a leitura das seguintes informações: quantidade de unidades de um produto
produzidas, valor (preço) de uma unidade desse produto e porcentagem de imposto a ser
paga. Depois calcule o valor do imposto a ser pago e imprima na tela esse valor obtido.
"""


quantidade_de_unidades = int(input("Digite a quantidade de unidades do produto produzidas: "))
valor_unidades = float(input("Digite o valor de uma unidade desse produto: R$"))
porcentagem_imposto = float(input("Digite a porcentagem do valor do imposto a ser pago (%): "))
unidades_valor_total = quantidade_de_unidades * valor_unidades
valor_imposto = unidades_valor_total * porcentagem_imposto / 100


print(f"Com o valor total dos produtos sendo R${unidades_valor_total:.2f} o valor do imposto será de: R${valor_imposto:.2f}")
