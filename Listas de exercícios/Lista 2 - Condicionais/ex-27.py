"""
Escreva um programa em Python que leia do teclado dois valores quaisquer, guardeos em duas variáveis ‘a’ e ‘b’ e, a seguir,
troque os valores associados a estas duas variáveis. 
O valor original armazenado em ‘b’ deve passar para ‘a’ e o valor original de ‘a’ deve passar para b.
Obs.: note que a sequência de comandos a=b; b=a; não vai funcionar! Por quê?
"""
a = int(input("Digite um número natural qualquer: "))
b = int(input("Digite outro número natural qualquer: "))


gambiarra = a
a = b
b = gambiarra
print(f"a = {a} e b = {b}")
