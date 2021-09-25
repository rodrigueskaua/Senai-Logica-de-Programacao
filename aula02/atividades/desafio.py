"""5. Desafio: Piso nos cômodos
Você foi contratado(a) para projetar a aplicação do piso de dois cômodos de uma casa: uma sala e um quarto.

5.1. Peça para o usuário informar a largura e o comprimento (em m) da sala. Mostre a área da sala em m².
5.2. Peça para o usuário informar a largura e o comprimento (em m) do quarto. Mostre a área do quarto em m².
5.3. Sabendo que custa R$30.00 por m² para aplicar piso em um cômodo, mostre quanto será gasto para colocar piso na sala e no quarto.
5.4. Sabendo que cada piso tem 0.25m² de tamanho, mostre quantos pisos (unidades) serão necessários para cobrir a sala e o quarto.
5.5. Mostre V ou F que a área dos cômodos é diferente.
5.6. Mostre V ou F que a soma da área dos cômodos é menor que 50m².
5.7. Mostre V ou F que será gasto menos de R$1000 em cada cômodo.
5.8. Mostre V ou F que serão necessárias pelo menos 100 unidades de piso em algum dos cômodos.

Informações e fórmulas úteis:
Preço de aplicação do piso = R$ 30.00 por m²
Tamanho do piso = 0.25 m²
Área do cômodo = Comprimento x Largura
Preço piso no cômodo = Área do cômodo x Preço m² do piso
Qtd. pisos p/ cômodo = Área do cômodo / Tamanho do piso"""

print('Digite as informações da SALA (em metro)')
sala_comprimento = float(input('Comprimento: '))
sala_largura = float(input('Largura: '))
area_sala = sala_comprimento * sala_largura
valor_sala = area_sala * 30.00
pisos_sala = area_sala / 0.25

print(f'A area da sala é {area_sala:.2f}m² \n')


print('Digite as informações do QUARTO (em metro)')
quarto_comprimento = float(input('Comprimento: '))
quarto_largura = float(input('Largura: '))
area_quarto = quarto_comprimento * quarto_largura
valor_quarto = area_quarto * 30.00
pisos_quarto = area_quarto / 0.25
print(f'A area do quarto é {area_quarto:.2f}m² \n')

print(f'O valor para colocar piso na sala e no quarto é de R${valor_sala + valor_quarto:.2f} \nSendo R${valor_sala:.2f} o valor para a sala e R${valor_quarto:.2f} o valor para o quarto \n')
print(f'A quantidade de pisos que serão necessários para cobrir a sala e o quarto é de {pisos_sala + pisos_quarto:.2f} \nSendo {pisos_sala:.2f} pisos para a sala e {pisos_quarto:.2f} pisos para o quarto \n')

print("A área dos cômodos é diferente?", area_sala != area_quarto) 
print("A soma da área dos cômodos é menor que 50m²?", (area_sala + area_quarto) < 50) 
print("Será gasto menos de R$1000 em cada cômodo?", valor_quarto < 1000 and valor_sala < 1000) 
print("Serão necessárias pelo menos 100 unidades de piso em algum dos cômodos?", pisos_sala >= 100 or pisos_quarto >= 100) 

