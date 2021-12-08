"""
2. Simule a execução do programa abaixo destacando sua saída, ou seja, o que exatamente será
impresso na tela. Você deve escrever na ordem em que os dados aparecem.

"""

def FazAlgo(x, y, vetor):
 c = y
 b = x % 4
 x = x + 2;
 y = y + 3
 print("\n {} {} {} {} {}".format(b, x, y, vetor[b], c))
 return y
a = 5
b = 6
c = 7
vetor = []
for i in range(4):
    vetor.append(i+a)
print("Os valores do vetor são: \n")
for i in range(4):
 print(vetor[i])
b = FazAlgo(a + c, b, vetor)
print("\n {} {} {}".format(a,b,c));