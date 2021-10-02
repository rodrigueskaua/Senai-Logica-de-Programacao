print("""Escolha o dia da semana para saber quanto tempo o Seu Madruga trabalha:
[ 1 ] DOM 
[ 2 ] SEG
[ 3 ] TER
[ 4 ] QUA
[ 5 ] QUI
[ 6 ] SEX
[ 7 ] SAB
""")

dia = int(input())

if dia == 2 or dia == 4 or dia == 6:
  print('Ele trabalha 8 horas por dia')

elif dia == 3 or dia == 5:
  print('Ele trabalha 10 horas por dia')
  
elif dia == 7 or dia == 1:
  print('Ele trabalha 0 horas por dia')
else: print("Erro!, a opção digitada não é válida.")
print("FIM DO PROGRAMA")