dist = float(input('Informe a distância (em km) até o detino\n'))

if dist>0:
    din=input('Você tem dinheiro? (S/N) \n')
    if din =="s" or din=="S":
        if dist <= 500:
            print(f"Para a distância de {dist}km a opção recomendada é ir de ônibus.")
        else:
            print(f"Para a distância de {dist}km a opção recomendada é ir de avião.")
    else:
        if dist <= 3 :
            print (f"Para a distância de {dist}km a opção recomendada é ir a pé.")
        elif dist > 3 and dist <= 20:
            print (f"Para a distância de {dist}km a opção recomendada é ir de bike.")
        else:
            print(f"Para a distância de {dist}km a opção recomendada é ir de carona.")
else:
    print('Distancia invalida')
print('Fim do programa.')