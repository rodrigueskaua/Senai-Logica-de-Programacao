lista_valores = []
num_quantidade = 0

while num_quantidade < 7:
    valor = int(input("Insira um novo valor "))
    lista_valores.append(valor)
    num_quantidade += 1

lista_valores.reverse()
print(lista_valores)


#Estrutura for
lista_valores = []

for i in range(7):
    valor = int(input("Insira um novo valor "))
    lista_valores.append(valor)


lista_valores.reverse()
print(lista_valores)
