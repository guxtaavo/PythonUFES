# Variações do print com váriaveis:
# fstrings e .format

nome = 'Gustavo'
idade = 30
verdadeiro = True

# print(f"{nome} tem {idade} anos {verdadeiro}")
# print(type(verdadeiro))
print("{} tem {} anos".format(idade, nome, verdadeiro))