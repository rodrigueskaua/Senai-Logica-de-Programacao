from datetime import date

ano_de_nascimento = int(input('Digite o ano de nascimento da pessoa de quem o ciclo será analisado: '))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento


if idade >= 2 and idade <= 5:
  print(f'A criança possui {idade} anos de idade')
  print('Ciclo de ensino atual: Infantil')
elif idade >=6 and idade <= 10:
  print(f'A criança possui {idade} anos de idade')
  print('Ciclo de ensino atual: Fund I')
elif idade >= 11 and idade <= 14:
  print(f'O pré-adolesente possui {idade} anos de idade.')
  print('Ciclo de ensino atual: Fund II')
elif idade >=15 and idade <= 17:
  print(f'O adolesente possui {idade} anos de idade')
  print('Ciclo de ensino atual: Médio')
else:
  print('Ciclo de ensino atual: Não detectado')