"""
Faça um programa em Python para converter um dado valor em reais (R$) para a
moeda dólar (US$). O programa deve ler um valor em reais (R$) e a cotação da moeda
americana, depois converter para dólares (US$) e apresentar este valor convertido na tela.
"""


valor_reais = float(input("Digite o valor em reais: R$"))
cotacao_dolar = float(input("Digite a cotação atual do dolar: R$"))

conversao = valor_reais / cotacao_dolar

print(f"O valor de R${valor_reais:.2f} convertido para dolares é ${conversao:.2f}")

