# email = "kauafelipe@gmail.com"
# tamanho_texto = len(email)
# print(email.split("@"))

# substitui um valor antigo por um novo
email = "  kauafelipe@gmail.com  "
print(email.split("@"))
print(email.replace("gmail" , "outlook"))
print(email.lower())
print(email.upper())
print(email.strip())


# Exemplo

nome = input("Informe seu nome e sobrenome")
lista = nome.split(" ")
print("Nome:", lista[0])
print("Sobrenome:", lista[1])
