"""
2. Escreva uma função que receba como parâmetro o ângulo que uma linha faz com o eixo positivo X e determina e
retorna o quadrante em que essa linha reside. A determinação do quadrante é dada através da seguinte tabela:

Ângulo com o eixo positivo X Quadrante
Entre 0 e 90 graus    | 1
Entre 90 e 180 graus  | 2
Entre 180 e 270 graus | 3
Entre 270 e 360 graus | 4

Se o ângulo for exatamente 0, 90, 180, ou 270 graus, a linha correspondente não reside em nenhum quadrante,
mas fica em cima de um eixo. Para esta situação, sua função deve retornar 0. Um ângulo fora do intervalo entre 0 e
360 deve resultar no retorno do valor –1. A função principal deve imprimir o valor retornado.

"""


def encontrarQuadrante(angulo):
    if angulo < 0 or angulo > 360:
        return -1
    elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270:
        return 0
    elif angulo > 0 and angulo < 90:
        return 1
    elif angulo > 90 and angulo < 180:
        return 2
    elif angulo > 180 and angulo < 270:
        return 3
    elif angulo > 270 and angulo < 360:
        return 4
    
    
angulo = int(input("Digite o ângulo  com o eixo positivo X: "))
print(f"Quadrante {encontrarQuadrante(angulo)}")