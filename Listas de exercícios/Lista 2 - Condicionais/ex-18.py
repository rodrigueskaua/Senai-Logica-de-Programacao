"""
18. Escreva um programa em Python para ajudar a calcular a quantidade de gotas de um
remédio que uma determinada criança precisa tomar. A bula desse remédio pediátrico
recomenda a seguinte dosagem: 5 gotas para cada 2 kg do peso da criança. Você deve
fazer um programa que leia o peso desta criança, calcule e imprima na tela a quantidade
de gotas a ser tomada.
"""


peso_criaca = float(input("Digite o peso da criança (kg): "))
gotas_quantidade = peso_criaca / 2 * 5

print(f"Para uma criança com {peso_criaca}kg a quantidade de gostas a ser tomadas é {gotas_quantidade}")