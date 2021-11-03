"""
21. Faça um programa em Python que leia a idade de uma pessoa expressa em anos,
meses e dias e mostre-a expressa apenas em dias. Assuma, neste programa, que um ano
tem 365 dias e que um mês tem 30 dias. Exemplo: Se a pessoa digitar que tem 28 anos 1
mês e 10 dias deverá aparecer na tela que ela viveu 10260 dias.
"""
print("""Digite sua idade como no exemplo:
Anos: 28
Meses: 10
Dias: 5

""")
anos_idade = int(input("""Digite sua idade:
Anos: """))

meses_idade = int(input("Meses: "))

dias_idade = int(input("Dias: "))

dias_totais = (anos_idade * 365) + (meses_idade * 30) + dias_idade

print(f"Você viveu {dias_totais} dias")