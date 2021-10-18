comida = 0
bebida = 0
print('='*30)
print(' LANCHONETE GOLZINHO VERMELHO')
print('='*30)

while comida == 0:
    print('\nVai querer o que pra comer?')
    comida += int(input("1) Sanduíche \n2) Bolo \n3) Pipoca\n"))
    if comida >= 1 and comida <= 3:
        print('Boa escolha')
        
    else:
        comida = 0
        print('Tente uma opção valida')

while bebida == 0:
    print('\nVai querer o que pra beber? ')
    bebida += int(input("1) Suco \n2) Refrigerante \n3) Água\n"))
    if bebida >= 1 and bebida <= 3:
        print('Boa escolha')
        
    else:
        bebida = 0
        print('Tente uma opção válida')
print('='*30)
print('''Agradecemos a preferência ^_^''')
print('='*30)