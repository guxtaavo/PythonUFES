# Podemos receber dados do usuário através da função input
# Por padrão chega tudo como str

idade = input('Digite a sua idade: ')
idade_convertida = int(idade)
print(type(idade_convertida))
print(type(idade))