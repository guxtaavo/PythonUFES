# Podemos receber dados do usuário através da função input
# Por padrão chega tudo como str

# idade chega como uma string
idade = input('Digite a sua idade: ')

# idade_convertida recebe o valor de idade mas na forma de um inteiro
idade_convertida = int(idade) 

print(type(idade_convertida))
print(type(idade))
