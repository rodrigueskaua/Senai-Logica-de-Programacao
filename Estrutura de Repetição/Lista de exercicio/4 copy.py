escolha = -1
pizza = int
while escolha < 0 or escolha > 5:

    escolha = int(input("O que você está achando do Python? \n1) Barril dobrado \n2) Barril \n3) Mais ou menos \n4) De Boa \n5) Muito de boa \n"))
    if escolha == 1 or escolha == 2:
        pizza = 1
        
    elif escolha == 3 or escolha == 4: 
        pizza = 2

    elif escolha == 5:
        pizza = 3 
    elif escolha == 0:
        print("Você escolheu uma opção pior que 'Barril dobrado', Sem pizza para você.")
        break
        
else: print(f"Fim do programa. Você ganhou {pizza} pizza(s)!!!. ")
