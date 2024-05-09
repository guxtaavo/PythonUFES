# Strings - Aspas simples / Aspas duplas
# Citações
# Docstrings - Aspas triplas
# Funciona como uma lista de caracteres - ìndice e tamanho
# Funções For e In

X = "Hello, World"
Y = 'Olá, Mundo'

# As citações ficam entre aspas dentro da string
Exemplo = 'Fulano disse "Etc"' 
print(Exemplo)

# Utilizar aspas triplas permite criar uma string de várias linhas
Docstring = """A
B
C
D
E
"""
print(Docstring)

tamanho = len(Docstring)
print(tamanho)

indice = X[11]
print(indice)

# Slice é um intervalo de índices
slice = X[-5:-2]
print(slice)

# O for é utilizado para rodar um caracter de cada vez
for x in X:
    print(x)

# O in permite saber se uma certa string está presente dentro de outra
if "World" in X:
    print("True")
