from datetime import date
print('Digite o ano logo abaixo ou digite 1 para analisar o ano atual')
ano = int(input("Digite o ano: "))
if ano == 1 :
    ano = date.today().year

if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
