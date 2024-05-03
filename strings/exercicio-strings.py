# Crie um programa que receba do usuário um conjunto de e-mails, 
# retorne se o formato recebido é válido, e caso seja, retorne também qual o serviço de e-mail utilizado
# Um email só será válido se for no formato nome@serviço.tipo e terminar com .com ou .br
# Ex: fulano@gmail.com - Saída: Válido - gmail

emails = input("Digite os emais separados por um espaço:\n")
emails = emails.split()
for email in emails:
    if ("@" in email and (email.endswith(".com") or email.endswith(".br"))):
        email = email.split("@")[1]
        print("Válido", email[email.find("@")+1:email.find(".")])
    else:
        print("Inválido")
        continue

