"""Escrever um programa que leia um número inteiro n e calcule e mostre a tabuada do n. Mostre a tabuada na forma: 
1 x n = n 
2 x n = 2n 
3 x n = 3n 
... 
10 x n = 10n
"""

print("=-=-=-TABUADA-=-=-=")
num = int(input("Digite um número para conferir a tabuado dele: "))
tabuada = 0
for l in range(0,10):
    tabuada+= 1
    print(f"{num} x {tabuada} = {num * tabuada} ")
print("-=" * 10)