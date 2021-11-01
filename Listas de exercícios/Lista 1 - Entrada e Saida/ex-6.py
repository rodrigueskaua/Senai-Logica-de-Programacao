"""
6. Corrija o seguinte programa em Python:
login = "Lucasfsa"
senha = "123"
print("O usuário informado foi: %d, e a senha digitada
foi: %s",(login, senha))
"""

# Com .format
login = "Lucasfsa"
senha = "123"
print("O usuário informado foi: {}, e a senha digitada foi: {}".format(login, senha))

# Com f""

login = "Lucasfsa"
senha = "123"
print(f"O usuário informado foi: {login}, e a senha digitada foi: {senha}")