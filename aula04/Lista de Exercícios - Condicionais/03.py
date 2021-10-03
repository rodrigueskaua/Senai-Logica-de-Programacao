print("Para cada pergunta a seguir, digite S para Sim. Outra tecla para Não \n")

pergunta1 = str(input("Você faz atividdade física regularmente? "))
if pergunta1 == "S" or pergunta1 == "s":
    print("Parabéns! continue assim \n")
else:
    print("Então essa é a hora de começar a se exercitar! \n")

pergunta2 = str(input("Você dorme pelo menos 8h por dia? "))
if pergunta2 == "S" or pergunta2 == "s":
    print("Ótimo! \n")
else:
    print("Cuidado! dormir menos de 8 horas pode trazer problemas para sua saúde \n")

pergunta3 = str(input("Você tem uma boa rotina alimentar? "))
if pergunta3 == "S" or pergunta3 == "s":
    print("Continue assim! \n")
else:
    print("Cuidado! Não ter uma boa rotina alimentar pode trazer problemas para sua saúde")

