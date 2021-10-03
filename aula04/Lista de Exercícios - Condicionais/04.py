saldo = float(5000.00)
escolha = int(input(f"""Você possui saldo inicial de R${saldo:.2f}
Para onde você deseja viajar?
[ 1 ] Brasil
[ 2 ] Exterior \n"""))

if escolha == 1 or escolha == 2:
    if escolha == 1:
        escolha_brasil = int(input(f"""Como quer viajar?
[ 1 ] Avião
[ 2 ] Cruzeiro \n"""))

        if escolha_brasil == 1:
            print(f"Viajando dentro país de avião o saldo restante é R${saldo - 1000:.2f}")
        elif escolha_brasil == 2:
            print(f"Viajando dentro país de Cruzeiro o saldo restante é R${saldo - 5000:.2f}")
        else:
            print("Erro!, a opção digitada não é válida.")

    elif escolha == 2:
        escolha_exterior = int(input(f"""Qual classe quer viajar?
[ 1 ] Classe econômica 
[ 2 ] Primeira classe \n"""))

        if escolha_exterior == 1:
            print(f"Viajando para o exterior de classe econômica o saldo restante é R${saldo - 2000:.2f}")

        elif escolha_exterior == 2:
            print(f"Viajando para o exterior de primeira classe o saldo restante é R${saldo - 4000:.2f}")

        else:
            print("Erro!, a opção digitada não é válida.")
else:
    print("Erro!, a opção digitada não é válida.")

