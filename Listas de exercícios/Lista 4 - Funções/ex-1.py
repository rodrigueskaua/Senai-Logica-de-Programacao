"""
1. Escreva um programa que leia um número e contenha uma função. Esta função deve receber por parâmetro um
número, verificar e retornar o valor 1 se o número for solução da equação 2x² - 7x + 3 = 0. Caso o número não
seja solução da equação, retornar o valor zero. A função principal deve recebe o valor de retorno e imprimir uma
mensagem informando se o valor é ou não solução da equaçãos
"""
def verificarNumero(n):
    equacao = 2 * n**2 - 7*n + 3 == 0
    if equacao == True:
        return 1
    else: 
        return 0

def principal(num):
    solução = verificarNumero(num)
    if solução == 1:
        print(f"O valor {num} é a solução da equação") 
    else: 
        print(f"O valor {num} não é a solução da equação")
    

numero = int(input("Digite o valor que é a solução da equação(x), 2x² - 7x + 3 = 0 \n"))
principal(numero)
