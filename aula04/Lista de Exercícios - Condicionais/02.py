tamanho_salg = str(input("Escolha o tamanho da peça: (M) Média ou G) Grande \n"))
tamanho_suco = str(input("Escolha o tamanho do suco: (M) Média ou G) Grande \n"))

if tamanho_salg == "M" and tamanho_suco == "M":
    print("Preço: R$10,00")

elif tamanho_salg == "M" and tamanho_suco == "G":
    print("Preço: R$12,00")

elif tamanho_salg == "G" and tamanho_suco == "M":
    print("Preço: R$13,00")
elif tamanho_salg == "G" and tamanho_suco == "G":
    print("Preço: R$15,00")

elif tamanho_salg != "M" and tamanho_salg != "G" or tamanho_suco != "M" and tamanho_suco != "G":
    print("Preço: R$ ?")


