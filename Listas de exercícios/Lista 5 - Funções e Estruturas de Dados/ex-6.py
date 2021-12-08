"""
Uma das maneiras de se conseguir a raiz quadrada de um número é subtrair do número os ímpares consecutivos a
partir de 1, até que o resultado da subtração seja menor ou igual à zero. O número de vezes que se conseguir
fazer a subtração é a raiz quadrada exata (resultado 0) ou aproximada do número (resultado negativo).

Exemplo: Raiz de 16
16 - 1 = 15 - 3 = 12 - 5 = 7 - 7 = 0 A raiz de 16 é 4
Escreva um programa que leia um inteiro e passe o valor por parâmetro para a função raiz(). A função raiz() utiliza
o método descrito acima para calcular e retornar a raiz inteira encontrada. A raiz encontrada deverá ser impressa
pelo programa principal.


"""
# def raiz(num):
#     contador = 0
#     for i in range(1,num):
#         if i % 3 == 0:
#             contador += 1
#     return contador
    
# def raiz(num):
    
#     for i in range(0,num):
#         resultado = verifica_numero_impar(n)
#         print(resultado)



# num = int(input("Digite um número inteiro: "))
# # print(raiz(num))

# num = 16
# contador = 0

# for i in range(16):
#     if i % 2 == 1:
#         num = num - i
# print(num)

        
# contador = 0
# for impar in range(16):
#     if impar % 2 == 1:
#         contador += 1
# print(contador)

num = 8

contador = 0


for impar in range(1,num +1):
    if impar % 2 == 1:
        num = num - impar
        contador += 1
        if num <= 0:
            break
print(contador)

        