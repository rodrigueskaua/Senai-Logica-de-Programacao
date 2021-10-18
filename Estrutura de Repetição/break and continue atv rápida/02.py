escolha = int
while True :
    escolha = int(input("""Digite o número referente a uma das quatro opções de lazer noturno:
[ 1 ] Jogar
[ 2 ] Assistir seriado
[ 3 ] Usar redes sociais
[ 4 ] Programar \n"""))
    if escolha == 1 or escolha == 2 or escolha == 3:
        continue    
    elif escolha == 4:
        print("Uma mentira foi detectada")
        break
    else: 
        print("Digite uma opção válida! \n")

