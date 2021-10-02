print('Digite as informações da SALA (em metros)')
sala_comprimento = float(input('Comprimento: '))
sala_largura = float(input('Largura: '))
area_sala = sala_comprimento * sala_largura
valor_sala = area_sala * 30.00
pisos_sala = area_sala / 0.25

print(f'A area da sala é {area_sala:.2f}m² \n')


print('Digite as informações do QUARTO (em metros)')
quarto_comprimento = float(input('Comprimento: '))
quarto_largura = float(input('Largura: '))
area_quarto = quarto_comprimento * quarto_largura
valor_quarto = area_quarto * 30.00
pisos_quarto = area_quarto / 0.25
print(f'A area do quarto é {area_quarto:.2f}m². \n')

print(f'O valor para colocar os pisos na sala e no quarto é de R${valor_sala + valor_quarto:.2f} \nSendo R${valor_sala:.2f} o valor para a sala e R${valor_quarto:.2f} o valor para o quarto. \n')
print(f'A quantidade de pisos que serão necessários para cobrir a sala e o quarto é de {pisos_sala + pisos_quarto:.1f} \nSendo {pisos_sala:.1f} pisos para a sala e {pisos_quarto:.1f} pisos para o quarto. \n')

print("A área dos cômodos é diferente?", area_sala != area_quarto) 
print("A soma da área dos cômodos é menor que 50m²?", (area_sala + area_quarto) < 50) 
print("Será gasto menos de R$1000 em cada cômodo?", valor_quarto < 1000 and valor_sala < 1000) 
print("Serão necessárias pelo menos 100 unidades de piso em algum dos cômodos?", pisos_sala >= 100 or pisos_quarto >= 100) 
