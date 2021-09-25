print("-=" * 20)
nome = str(input('Digite seu nome completo: '))
altura = float(input('Digite sua altura (em metros): '))
calçado = int(input('Digite o número que você calça: '))

altura += 0.10
calçado += 2
print("-=" * 20)
print(f'Seu nome completo é {nome}')
print(f'Sua nova altura é {altura:.2f}')
print(f'Seu novo número do calçado é {calçado}')
print("-=" * 20)


