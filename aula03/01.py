valor = float(input('Digite o valor da comprar: R$'))
cupom = str(input('Você possui cupom de desconto? (S/N) \n' ))
if cupom == "S" or cupom == "s" :
    valor = valor - (valor * 0.10)
    
print(f"O valor final da compra é R${valor:.2f}")