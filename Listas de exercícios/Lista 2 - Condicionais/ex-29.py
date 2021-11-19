"""
29. Uma agência de viagens quer disponibilizar a seus passageiros que chegam ao Brasil
um terminal de conversão de taxa de câmbio. Tal terminal será utilizado num aeroporto
que recebe principalmente passageiros norte-americanos, europeus e japoneses. Escreva
um programa em Python que leia do teclado a opção desejada: converter dólares, euros
ou ienes para reais, leia a quantia em moeda estrangeira e apresente na tela o valor dado
e seu equivalente em reais.
Considere:
1,00 DÓLAR = R$ 4,12
1,00 EURO = R$ 4,59
1,00 IENE = R$ 0,038
"""

moeda = "?"
conversao = 0
moeda_opção = int(input("""Digite o número da opção de moeda para a conversão em reais
(1) DÓLAR
(2) EURO
(3) IENE 
Opção: """))

valor = float(input("Digite o valor da quantia para ser convertida para reais: $"))

if moeda_opção == 1:
    conversao = valor * 4.12
    moeda = "$"
elif moeda_opção == 2:
    conversao = valor * 4.59
    moeda = "€"

elif moeda_opção == 3:
    conversao = valor * 0.038
    moeda = "¥"
else: print("ERRO!, moeda não identificada")


print(f"O valor de {moeda}{valor:.2f} convertido para reais é R${conversao:.2f}")
