"""
Faça uma função que, dado um número representando uma temperatura em graus Fahrenheit, retorne a
temperatura em Celsius. Obs: C=(5/9)*(F-32)
"""

f = float(input("Digite a temperatura em graus fahrenheit: "))
def celsius(f):
    c = (5/9)*(f-32)
    return c

c = celsius(f)
print(f"A temperatura de {f} graus fahrenheit convertida para graus celcius é: {c:.2f}")