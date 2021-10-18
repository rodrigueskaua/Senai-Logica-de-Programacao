print("Questionário sobre o voto obrigatório no Brasil")

pergunta1 = str
pergunta2 = str

while pergunta1 != "B" and  pergunta1 != "b":

    pergunta1 = str(input("1) As pessoas de qual nacionalidade são obrigadas a votar no Brasil? \nA) Argentina \nB) Brasileira \nC) Chilena \n"))

while pergunta2 != "C" and  pergunta2 != "c":

    pergunta2 = str(input("2) Qual faixa etária é obrigada a votar no Brasil? \nA) 10~18 anos \nB) 70~80 anos \nC) 18~70 anos \n"))

else:
    print("Fim do questionário")
  