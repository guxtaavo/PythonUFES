# Principais Métodos:
# Upper / Lower
# Strip
# Replace
# Split

# O upper deixa todas as letras maiúsculas / O lower deixa todas as letras minúsculas
X = "Hello, World123?@"
Y = X.lower()
print(Y)

# O strip remove os espaços em branco no início e no final (Se colocarmos alguma string entre parênteses, essa string que será removida das extremidades)
Blank = "  Qualquer Coisa   "
print(Blank.strip())

# O replace serve para substituir uma string por outra
Z = X.replace("123?@","")
print(Z)

# O split serve para separar uma string em uma lista de strings (Se deixarmos vazio entre parênteses, iremos separar os espaços vazios " ")
W = Z.split(",")
print(W)
