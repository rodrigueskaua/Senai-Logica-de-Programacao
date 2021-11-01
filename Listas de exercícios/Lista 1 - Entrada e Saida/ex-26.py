"""
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""
# Quantas vezes a letra (A) aparece
frase = str(input('Digite uma frase: ')).upper().strip()
frase_a = frase.count('A')
print(f'A letra (a) aparece {frase_a} vezes na frase.')

# Primeira posição onde o (A) aparece
a1 = frase.find('A')+1
print(f'A primeira letra (a) apareceu na posição {a1}')

# Última posição onde o (A) aparece
a2 = frase.rfind('A')+1
print(f'A última letra (a) apareceu na posição {a2}')
