# Em Python, os operadores lógicos são utilizados para combinar duas ou mais expressões.

# Os operadores lógicos são:
# and (e)
# or (ou)
# not (não)

# Exemplos:

# and (utilizado para verificar se a combinação de duas ou mais expressões é verdadeira)
a = 2
b = 2
print(a == 2 and b == 2) # True

# Fazendo b = 3
b = 3
print(a == 2 and b == 2) # False
# Como a segunda expressão é falsa, o resultado é False
# Ainda é possível criar mais expressões
c = 2
print(a == 2 and b == 2 and c == 2) # False
# Como a segunda expressão é falsa, o resultado é False



# or (utilizado para verificar se pelo menos uma das expressões é verdadeira)
a = 2
b = 3
print(a == 2 or b == 2) # True
# Como a primeira expressão é verdadeira, o resultado é True
# Fazendo a = 3 e b = 2
a = 3
b = 2
print(a == 2 or b == 2) # True
# Como a segunda expressão é verdadeira, o resultado é True
# Colocando outra expressão
c = 3
print(a == 2 or b == 2 or c == 2) # True
# Como a segunda expressão é verdadeira, o resultado é True



# not (utilizado para inverter o valor da expressão)
a = 2
print(not a == 2) # False
# a == 2 de fato é verdadeiro, mas o not inverte o valor, tornando falso
b = 2
print(not b == 3) # True
# b == 3 de fato é falso, mas o not inverte o valor, tornando verdadeiro
print (not (a == 2 and b == 2)) # False
# Como a expressão é verdadeira, o resultado é False