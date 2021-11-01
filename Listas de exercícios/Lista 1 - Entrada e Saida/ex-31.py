"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

dis = int(input("Digite a distância da viagem: "))
if dis <= 200 :
    km = dis * 0.50 
    print(f'O valor total da passagem é R${km:.2f}')
else: 
    km = dis * 0.45
    print(f'O valor total da passagem é R${km:.2f}')
