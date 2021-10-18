"""
4. Escreva um programa que o usuário informe o que acha de Python: 1) Muito barril, 2) Barril, 3) Mais ou Menos, 4) De boa, 5) Muito de boa.
→ Se o usuário digitar 1 ou 2, o programa exibe fora do while (na mensagem de fim de programa) que ganhou uma pizza.
→ Se o usuário digitar 3 ou 4, o programa exibe fora do while (na mensagem de fim de programa) que ganhou duas pizzas.
→ Se o usuário digitar 5, o programa exibe fora do while (na mensagem de fim de programa) que ganhou três pizzas.
→ Se o usuário digitar 0, o programa tem uma saída inesperada e diz que o usuário ficará sem pizzas.
→ Se o usuário digitar outro número, o programa pede para digitar novamente.
"""



escolha = -1
pizza = int
while not escolha >= 0 and escolha <= 5 :  
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

"""lazer = 0
while True:
  lazer = int(input("\nO que você vai fazer?\n1) Jogar\n2) Assistir série\n3) Usar redes sociais\n4) Programar\n"))
  if lazer >= 1 and lazer <= 3:
    print("Poxa, que massa! Hehehe!")
    continue
  elif lazer == 4:
    print("Larga de mentira! :)")
    break
  else:
    print("Digite uma opção válida!")"""