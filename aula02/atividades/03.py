print("-=" * 30)

junho = float(input('Digite o valor do salário do mês de junho:  R$'))
julho = float(input('Digite o valor do salário do mês de julho:  R$'))
jun_jul = (junho + julho) / 2

print(f'A média salarial do bimestre junho-julho é  R${jun_jul:.2f}')
print("-=" * 30)

agosto = float(input('Digite o valor do salário do mês de agosto:    R$'))
setembro = float(input('Digite o valor do salário do mês de setembro:  R$'))
ago_set = (agosto + setembro) / 2

print(f'A média salarial do bimestre agosto-setembro é R${ago_set:.2f}')
print("-=" * 30)

print("A média de junho-julho foi menor do que agosto-setembro? \n", jun_jul < ago_set)
print("A média em ambos bimestres foi maior que R$2000.00? \n", jun_jul > 2000.00 and ago_set > 2000.00)
print("A média em algum dos bimestres foi de pelo menos R$2500.00? \n", jun_jul >= 2500.00 or ago_set >= 2500.00)
print("-=" * 30)
