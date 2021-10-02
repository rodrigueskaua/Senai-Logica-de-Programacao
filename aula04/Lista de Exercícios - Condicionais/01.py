"""
1. Escreva um programa que o usuário informa a sigla de um estado (por ex.: BA, CE, PE).
→ O programa então informa qual é a capital daquele estado.
→ Faça para 5 estados quaisquer.
→ Se o usuário informar algo errado, diga que a opção é inválida.
→ Ao final, exiba uma mensagem de fim de programa.

"""

print("""Escolha o estado:
[ 1 ] BA
[ 2 ] MG
[ 3 ] ES
[ 4 ] PI
[ 5 ] AM
""")

estado = int(input())

if estado == 1:
  print('A capital do estado da Bahia é Salvador')

elif estado == 2:
  print('A capital do estado de Minas Gerais é Belo Horizonte')

elif estado == 3:
  print('A capital do estado do Espírito Santo é Vitória')

elif estado == 4:
  print('A capital do estado do Piauí é Teresina')
  
elif estado == 5:
  print('A capital do estado do Amazonas é Manaus')
else: print("Erro!, a opção digitada não é válida.")

print("FIM DO PROGRAMA")