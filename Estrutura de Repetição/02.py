tamanho_salg = str(input("Escolha o tamanho da peça: (M) Média ou G) Grande \n"))
tamanho_suco = str(input("Escolha o tamanho do suco: (M) Média ou G) Grande \n"))
valor = float

if tamanho_salg == "M" and tamanho_suco == "M":
    valor = float(10)

elif tamanho_salg == "M" and tamanho_suco == "G":
    valor = float(12)


elif tamanho_salg == "G" and tamanho_suco == "M":
    valor = float(13)

elif tamanho_salg == "G" and tamanho_suco == "G":
    valor = float(15)

elif tamanho_salg != "M" and tamanho_salg != "G" or tamanho_suco != "M" and tamanho_suco != "G":
    print("Preço: R$ ?")

elif tamanho_salg == "M" and tamanho_salg == "G" or tamanho_suco == "M" and tamanho_suco == "G":
    print(f"Preço: R${valor:.2f}")


