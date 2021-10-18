menu = input("Escolha uma opção: \n1) Continuar no laço \n2) Sair pelo else \n3) Sair pelo break \n")
while True:
      if menu == 1:
            menu = input("Escolha uma opção: \n1) Continuar no laço \n2) Sair pelo else \n3) Sair pelo break \n")
            continue
      elif menu == 3:
            print("saida inesperada")
            break
      elif menu == 2:
            print("saida normal")