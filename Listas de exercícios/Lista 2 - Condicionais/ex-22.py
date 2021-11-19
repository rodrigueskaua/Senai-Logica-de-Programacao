"""22. Um aluno deseja saber qual a porcentagem de faltas que ele tem em cada disciplina.
Ajude este aluno para que ele sempre possa calcular sua porcentagem de faltas. Para
isso, escreva um programa em Python que leia a carga horária da disciplina e a
quantidade de horas de faltas acumuladas, calcule a porcentagem e a imprima na tela."""


carga_horaria = float(input("Digite a carga horária da disciplina (horas): "))
faltas_acumuladas = float(input("Digite a quantidade de horas de faltas acumuladas (horas): "))
porcentagem =  faltas_acumuladas * 100 / carga_horaria


print(f"""O percentual é de {porcentagem:.2f}%
Para o total de {carga_horaria} horas de carga horária sobre {faltas_acumuladas} horas faltadas o percentual é de {porcentagem:.2f}%.""")


