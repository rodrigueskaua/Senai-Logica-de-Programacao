lista_valores = []
num_quantidade = 0

while num_quantidade < 7:
    valor = int(input("Insira um novo valor "))
    lista_valores.append(valor)
    num_quantidade += 1

lista_valores_inversos = lista_valores[::-1]

print(lista_valores_inversos)
