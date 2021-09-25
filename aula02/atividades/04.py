nota_log = float(input('Digite a sua nota final de Lógica de Programação: '))
nota_ti = float(input('Digite a sua nota final de Fundamentos de TI: '))
nota_web = float(input('Digite a sua nota final de Fund. Web Design: '))

print('')

print('A nota de Lógica de Programação não é igual a 10?', not nota_log == 10)
print('A nota de Fundamentos de TI é igual a 8.5?',  nota_ti == 8.5)
print('A nota de Fund. Web Design está entre 8 e 9?',  nota_web > 8.0 and nota_web < 9.0)
print('Todas as notas foram pelo menos 7?',  nota_web >= 7.0 and nota_log >= 7.0 and nota_ti >= 7.0)
print('Pelo menos uma nota foi maior do que 9.5?', nota_web > 9.5 or nota_log > 9.5 or nota_ti > 9.5)

print('')

media = (nota_log + nota_ti + nota_web) / 3
print(f'A média das notas é igual a {media:.2f}')
print(f'O tipo da variável que guarda a média é {type(media)}')

