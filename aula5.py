# Variações do print com váriaveis:
# fstrings e .format

nome = 'Gustavo'
idade = 30
instituicao = 'UFES'

# CONCATENAÇÃO
# frase = nome + ' ' + idade + ' ' + instituicao
# print(frase)

# FSTRINGS
# frase = f"{nome} tem {idade} anos e estuda na {instituicao}."
# print(frase)

# .FORMAT
# frase = "{} tem {} anos e estuda na {}.".format(nome, idade, instituicao)

# .FORMAT IGNORA ARGUMENTOS QUE EXCEDAM A QUANTIDADE DE COLCHETES 
# print("{} tem {} anos e estuda na {}.".format(idade, nome, instituicao, nome))
#      0       1                   2           0      1       2

# AQUI FALTA ARGUMENTOS PARA PASSAR NO .FORMAT, VAI DAR ERRO!
# print("{} tem {} anos e estuda na {}.".format(idade, nome))