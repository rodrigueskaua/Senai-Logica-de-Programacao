print("""Digite a opção:
[ 1 ] BA
[ 2 ] MG
[ 3 ] ES
[ 4 ] PI
[ 5 ] AM
""")

escolha = int(input())
capital = str

if escolha == 1:
    capital = "Salvador"

elif escolha == 2:
    capital = "Belo Horizonte"

elif escolha == 3:
    capital = "Vitória"

elif escolha == 4:
    capital = "Teresina"

elif escolha == 5:
    capital = "Manaus"

else:
    print("Erro!, a opção digitada não é válida.")

print(f"A capital do estado escolhido é {capital}.")
print("FIM DO PROGRAMA")
