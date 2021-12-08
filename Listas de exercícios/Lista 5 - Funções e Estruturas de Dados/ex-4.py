"""
Escreva um programa que chame uma função que deve receber por parâmetro dois valores (um para comprimento
e outro para largura), calcular e apresentar na tela a área de um retângulo, através da fórmula do retângulo =
comprimento * largura. Repetir a chamada da função com a passagem de parâmetros enquanto não for digitado
um número negativo para o comprimento ou para a largura.

"""
def areaRetangulo(comprimento ,largura):
    area = largura * comprimento
    return area


comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite o largura do retângulo: "))

while largura >=0 and comprimento >=0:
    resultado = areaRetangulo(comprimento,largura)
    print(f'A área do retângulo é {resultado}')
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite o largura do retângulo: "))