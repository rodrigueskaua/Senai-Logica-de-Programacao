# for contador in range(50, 201, 2):
#     print(contador)

soma = 0
n = int(input("Digite um número natural: "))
for i in range(1, n+1):
    soma += i
print(f"A soma dos naturais até {n} é {soma}.")
