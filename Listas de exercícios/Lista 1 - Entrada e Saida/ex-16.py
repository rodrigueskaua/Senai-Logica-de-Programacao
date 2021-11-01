"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

"""
from math import trunc
valor = float(input('Digite o valor: '))

print(f'O valor digitado foi {valor} e a sua porção inteira é {trunc(valor)}')