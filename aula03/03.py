"""3. Escreva um programa que sugere o modo de transporte da pessoa de acordo com a distância até o destino e a disponibilidade de dinheiro. 
→ Inicialmente, o programa pede para a pessoa informar a distância (em km) até o destino. Se um número inválido (0 ou menos) for digitado, o programa é encerrado.
→ Mas se uma distância válida for informada, então o programa pergunta se a pessoa tem dinheiro para o trajeto.
→ Caso a pessoa digite S (para “Sim”), o programa verifica:
→ Para distância de até 500 km, sugere ir de ônibus.
→ Caso contrário, sugere ir de avião.
→ Caso a pessoa digite uma resposta diferente de S, então:
→ Para distância de até 3 km, sugere ir a pé.
→ Para distância acima de 3 km e até 20 km, sugere ir de bike.
→ Caso contrário, sugere ir de carona.
"""
dist = float(input('Informe a distância (em km) até o detino\n'))
din = input('Você tem dinheiro? (S/N) ')

if dist > 0 and din == "S" or din == "s" : 
    if dist <= 500:
      print(f"Para a distância de {dist}km a opção  recomendada é ir de ônibus.")
    else: print(f"Para a distância de {dist}km a opção  recomendada é ir de avião.")

elif din != "S" or din != "s" and din >= 3:
    print(f"Para a distância de {dist}km a opção  recomendada é ir a pé.")

elif din != "S" or din != "s" and din > 3 and din <= 20:
    print(f"Para a distância de {dist}km a opção  recomendada é ir de bike.")

else:  print(f"Para a distância de {dist}km a opção  recomendada é ir de carona.")

print('Programa encerrado')

"""
if dist > 0 and din == "S" or din == "s" : :
    if dist <= 500:
      print(f"Para a distância de {dist}km a opção  recomendada é ir de ônibus.")

    elif din != "S" or din != "s":
      if din >= 3:
        print(f"Para a distância de {dist}km a opção  recomendada é ir a pé.")
    elif din > 3 and din <= 20:
      print(f"Para a distância de {dist}km a opção  recomendada é ir de bike.")
    else: print(f"Para a distância de {dist}km a opção  recomendada é ir de avião.")
  else:  print(f"Para a distância de {dist}km a opção  recomendada é ir de carona.")
print('Programa encerado')
"""