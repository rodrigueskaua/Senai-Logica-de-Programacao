import pandas

emails = open("emails.txt")
list_emails = sorted(emails.read().lower().replace("\n","").split(";"))
print("Quantidade de e-mail", len(list_emails))
assinaturas = pandas.read_csv("Lista de Presença.csv")
for email in list_emails:
    if email in assinaturas["Nome de usuário"].values:
        print(email, "Presente")
    else:
        print(email, "Ausente")