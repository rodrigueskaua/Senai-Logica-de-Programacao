"""
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')

n = nome.split()
ultimo = n[len(n)-1] 
print(f'Seu primeiro nome é {n[0]}')

print(f'Seu último nome é {ultimo}')

