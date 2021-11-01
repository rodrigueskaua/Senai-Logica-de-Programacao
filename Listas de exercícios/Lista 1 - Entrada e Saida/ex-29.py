"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
"""
print('--INICIANDO CALCULADORA DE MULTA--')
ve = int(input('Digite a velocidade do carro: '))

multa =(ve - 80) * 7.00

if ve > 80 :
    print('Você foi multado!')
    print(f'No valor de R${multa:.2f}')
else: 
    print('O limite de velocidade foi respeitado')
print('--DESLIGANDO CALCULADORA DE MULTA--')
