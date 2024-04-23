# Crie um programa que receba do usuário separadamente o nome, 
# o sobrenome, o dia, o mês (número) e o ano de nascimento. 
# Em seguida, mostre na tela o seguinte resultado:
# Nome: nome sobrenome
# Data de Nascimento: dia/mês/ano

# Defina se irá usar aspas simples ou duplas no seu código, para que fique
# padronizado, misturamos para que você veja que da certo com ambas.
nome = input('Digite o seu nome: ')
sobrenome = input("Digite o seu sobrenome: ")
# Você não precisa transformar o dia/mes/ano para int, pois
# não iremos fazer nenhuma operação aritmética com os dados informados
# poderia ser tudo padrão str.
dia_de_nascimento = int(input('Digite o seu dia de nascimento: ')) 
mes_de_nascimento = int(input("Digite o seu mes de nascimento: "))
ano_de_nascimento = int(input('Digite o seu ano de nascimento: '))

print(f"Nome: {nome} {sobrenome}")
print(f"Data de Nascimento: {dia_de_nascimento}/{mes_de_nascimento}/{ano_de_nascimento}")
