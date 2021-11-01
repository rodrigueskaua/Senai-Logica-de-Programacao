"""Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome."""


nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

maisculas = (nome.upper())
minusculas = (nome.lower())

print(f'Seu nome em maiscúlas é {maisculas}')
print(f'Seu nome em minúsculas é {minusculas}')

letras = len(nome.replace(" ", ""))
print(f'Seu nome tem {letras} letras')

primeiro = nome.split()

print(f'Seu primeiro nome é {primeiro[0]} e ele tem {len(primeiro[0])} letras')