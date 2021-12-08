"""
Escreva um programa para ajudar profissionais da área esportiva a calcular o valor da frequência cardíaca mínima
de treinamento para potência aeróbica. Escreva um programa que contenha uma função. Esta função deve
receber por parâmetro dois valores (os valores da idade e da frequência cardíaca de repouso (FCR)), calcular a
frequência cardíaca mínima de treinamento para potência aeróbica e retornar o valor encontrado. Repetir a
chamada da função com a passagem de parâmetros e impressão do resultado enquanto não for digitado um
número negativo para a idade.
Dado: FCT = FCR + 0.6 x ((220 – idade) – FCR)
"""

def FCT(idade ,fcr):
    ftc = fcr + 0.6 * ((220 - idade) - fcr)    
    return ftc


idade = float(input("Digite a idade: "))
fcr= float(input("Digite a frequência cardíaca de repouso (FCR): "))
print(FCT(idade,fcr))


while idade >=0:
    resultado = FCT(idade ,fcr)
    print(f'A frequência cardíaca mínima de treinamentoo é {resultado}')
    idade = float(input("Digite a idade: "))
    fcr= float(input("Digite a frequência cardíaca de repouso (FCR): "))
