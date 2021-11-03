"""
Um grupo de amigos pretende alugar um carro por um único dia. Consultadas duas
agências, a primeira cobra R$62,00 pela diária e R$1,40 por quilômetro rodado. A segunda
cobra diária de R$80,00 e mais R$1,20 por quilômetro rodado. Escreva um programa em
Python que leia a quantidade de quilômetros a serem rodados e calcule e imprima na tela
o preço a ser pago em cada uma das agências.

"""

km_rodado = float(input("Digite a quantidade de kilometros a serem rodados: "))
valor_agencia1 = 62 + (1.40 * km_rodado)
valor_agencia2 = 80 + (1.20 * km_rodado)


print(f"""Para {km_rodado}km o valor para alugar o carro é:
Primeira agência R${valor_agencia1:.2f}
Segunda agência R${valor_agencia2:.2f}.""")