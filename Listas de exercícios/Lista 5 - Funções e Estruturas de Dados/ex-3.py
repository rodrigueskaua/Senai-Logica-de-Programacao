"""
3. Escreva um programa que leia um número A (representando o número de alqueires) e uma letra (P para Paulista,
M para Mineiro e B para Baiano). O programa deve chamar uma função que recebe por parâmetro o número A e o
caractere lido, e converte A para um valor em metros quadrados, e retorna o valor encontrado segundo as
informações dadas logo abaixo. A função principal deve mostrar na tela o valor retornado.
Dado: 
Dado: 
1 alqueire Paulista = 24200 m²
1 alqueire Mineiro = 48400 m²
1 alqueire baiano = 96 800 m²
2

"""
def converterMetros(num,letra):
    metros_quadrados = 0
    if letra == "P":
        metros_quadrados = num * 24200
    elif letra == "M":
        metros_quadrados = num * 48400
    elif letra == "B":
        metros_quadrados = num * 96800
    else: 
        print("Valores inválidos")

    print(f"{metros_quadrados:.2f}") 

        
numA = float(input("Digite o número de alqueires: \n"))
letra = str(input("Digite a letra que representa o estado ( P ) para Paulista,( M ) para Mineiro e ( B ) para Baiano: \n"))
converterMetros(numA,letra)



