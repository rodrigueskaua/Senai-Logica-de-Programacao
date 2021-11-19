"""
13. Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada m2
deve-se usar 18 W de potência. Escreva um programa em Python que leia as dimensões
de um cômodo retangular (em metros), calcule e mostre a sua área (em m2) e a potência
de iluminação que deverá ser utilizada.
"""
print('Digite as informações do cômodo (em metros)')

comodo_comprimento = float(input('Comprimento: '))
comodo_largura = float(input('Largura: '))
comodo_area = comodo_comprimento * comodo_largura
potencia_iluminacao = comodo_area * 18

print(f'A área da cômodo é {comodo_area:.2f}m². \nA potência de iluminação que deverá ser utilizada é {potencia_iluminacao:.2f} W.')
