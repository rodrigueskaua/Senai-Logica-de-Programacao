"""Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
print('--INÍCIO--')
print("Tente adivinhar o número que estou pensando entre 0 e 5")

n = int(input('Qual é o número: '))
aleatorio = randint(0,5)
if n == aleatorio :
    print('ACERTOU!!!')
else: 
    print('ERRROOUU!!!')
    print(f'O número correto era {aleatorio}')

print('--FIM--')

print('Reset para jogar novamente')