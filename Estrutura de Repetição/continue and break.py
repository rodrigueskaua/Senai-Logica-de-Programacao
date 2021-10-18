"""numero = 0
while True:
    numero += 1
    print(f"Número: {numero}")
    if numero == 1000:
        break
print("Fim do programa")"""


"""
curso = str
while curso != "DS":
    curso = input('Qual é o melhor curso técnico? \n')
    if curso == "nenhum" or curso == "Nenhum":
        print('Você não gosta de estudar!')
        break
print("Fim do programa!")
"""

"""andar = 0
while True:
    andar += 1
    if andar == 13:
        continue
    print(f"ANDAR {andar}")
    if andar == 20:
        break
print("Você chegou no último andar!")"""
"""
andar = 0
while andar < 20:
    andar += 1
    if andar == 13:
        continue
    print(f"ANDAR {andar}")
print("Você chegou no último andar!")
"""

local = str
while True:
    local = input("Qual local você gostaria de visitar um dia? \n")
    if local == "FEIRA":
        print("Você já mora aí, poxa!")
        continue
    elif local == "NENHUM":
        print("Ok, você não gosta de viajar!")
        break
    print(f"Espero que você consiga visitar {local}")

