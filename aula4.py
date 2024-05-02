# Podemos receber dados do usuário através da função input
# Por padrão chega tudo como str

idade = input('Digite a sua idade: ') # idade chega como uma string
idade_convertida = int(idade) # idade_convertida recebe o valor de idade mas na forma de um inteiro
print(type(idade_convertida))
print(type(idade))
