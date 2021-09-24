"""Escreva um programa que peça o nome completo, a altura (em metros) e o número do calçado de uma pessoa. Em seguida: 
Acrescente 10 cm à altura da pessoa
Acrescente em 2 o número do calçado da pessoa 
Exiba o nome completo, a nova altura e o novo número do  calçado"""

print("-=" * 20)
nome = str(input('Digite seu nome completo: '))
altura = float(input('Digite sua altura: '))
calçado = int(input('Digite o número que você calça: '))

altura += 0.10
calçado += 2
print("-=" * 20)
print(f'Seu nome completo é {nome}')
print(f'Sua nova altura é {altura:.2f}')
print(f'Seu novo número do calçado é {calçado}')
print("-=" * 20)


