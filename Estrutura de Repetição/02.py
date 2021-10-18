tamanho_salg = str(input("Escolha o tamanho da peça: (M) Média ou G) Grande \n"))
tamanho_suco = str(input("Escolha o tamanho do suco: (M) Média ou G) Grande \n"))
valor = "?"

if tamanho_salg == "M" and tamanho_suco == "M":
    valor = "10"

elif tamanho_salg == "M" and tamanho_suco == "G":
    valor = "12"


elif tamanho_salg == "G" and tamanho_suco == "M":
    valor = "13"

elif tamanho_salg == "G" and tamanho_suco == "G":
    valor = "15"

elif tamanho_salg != "M" and tamanho_salg != "G" or tamanho_suco != "M" and tamanho_suco != "G":
    print("Preço: R$ ?")


print(f"Preço: R${valor},00")

