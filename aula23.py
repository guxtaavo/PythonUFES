# Escopo de váriaveis

# ESCOPO LOCAL
def funcao():
    idade = 2
    print(idade)

# ESCOPO RAIZ/ GLOBAL 
idade = 10

if idade > 10:
    msg = 'velho'
else:
    msg = 'novo'

for i in range(2):
    idade = i

print(msg)
print(idade)
funcao()