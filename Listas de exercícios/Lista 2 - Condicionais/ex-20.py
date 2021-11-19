"""
20. Escreva um programa em Python que solicita ao usuário duas datas (dia, mês, ano),
onde a primeira data é o dia atual e a segunda é a data de vencimento de suas contas, em
seguida o seu programa deve imprimir se a conta em questão “está atrasada”, “não está
atrasada” ou “vence neste dia”. Assuma que o usuário informa duas datas válidas.
"""

data_atual = [int(input("Digite o dia atual: ")), int(input("Digite o mês atual: ")), int(input("Digite o ano atual: "))]
data_vencimento = [int(input("Digite o dia do vencimeto: ")), int(input("Digite o mês do vencimeto: ")), int(input("Digite o ano do vencimeto: "))]

if data_atual == data_vencimento:
    estado_da_conta = "vence neste dia"

elif data_atual < data_vencimento:
    estado_da_conta = "não está atrasada"

elif data_atual > data_vencimento:
    estado_da_conta = "está atrasada"

print(f"A conta {estado_da_conta}.")