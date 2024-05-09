# Outros Métodos:
# Capitalize 
# Count
# Find
# Isalpha / Isnumeric
# Endswith / Startswith

# O capitalize deixa apenas a primeira letra da string maiúscula, e o restante minúscula
X = "12 345"
print(X.capitalize())

# O count conta quantas vezes um caracter se repete
contagem = X.count("L")
print(contagem)

# find encontra qual o índice em que um caracter aparece pela primeira vez
print(X.find("l"))

# isalpha pergunta se todos os caracteres são letras e isnumeric pergunta se todos os caracteres são números
print(X.isnumeric())

# startswith pergunta qual o começo de uma string e endswith pergunta qual o final
print(X.startswith("12"))
print(X.endswith("12"))
