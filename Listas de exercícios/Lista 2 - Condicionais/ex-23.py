"""23. Um hotel com 80 apartamentos deseja fazer uma promoção especial de final de
semana, concedendo um desconto de 25% na diária. Com isto, espera aumentar sua taxa
de ocupação de 50% para 80%. Sendo dado o valor normal da diária, escreva um
programa em Python que calcule e imprima:
a) o valor da diária promocional;
b) valor total arrecadado com 80% de ocupação e diária promocional;
c) o valor total arrecadado com 50% de ocupação e diária normal;
d) a diferença entre estes dois valores.

Exemplo:
Se for digitado o valor de 50 reais para a diária normal devemos imprimir na tela:
Diária promocional = 37.5
Total arrecadado com 80% de ocupação e diária promocional = 2400
Total arrecadado com 50% de ocupação e diária normal = 2000
Diferença entre os valores: 400"""

diaria = float(input("Digite o valor da diária normal: R$"))
valor_com_desconto = diaria - (diaria * 0.25) 
valor_arrecadado_80 =  80 * (80 / 100) * valor_com_desconto
valor_arrecadado_50 =  80 * (50 / 100) * diaria
diferenca_valores = valor_arrecadado_80 - valor_arrecadado_50


print(f"""Diária promocianal: R${valor_com_desconto:.2f}
Total arrecadado com 80% de ocupação e diária promocional: R${valor_arrecadado_80:.2f}
Total arrecadado com 50% de ocupação e diária normal: R${valor_arrecadado_50:.2f}
Diferença entre os valores: R${diferenca_valores:.2f}""")