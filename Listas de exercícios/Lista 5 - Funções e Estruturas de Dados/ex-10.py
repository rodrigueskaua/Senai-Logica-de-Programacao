"""
10. Faça uma função para calcular x elevado a y, sendo y inteiro e não negativo. Use produtos sucessivos para resolver
a questão.
"""
n1 = float(input("Insira o número: "))
n2 = int(input("Insira o expoente do número: "))


for i in range(n2):
    contador = n1 * {n1}
    
    resultado = n1


print(f"{n1}^{n2} = {resultado}")
