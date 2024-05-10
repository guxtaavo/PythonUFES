# Um bloco condicional é uma estrutura de controle que permite que você tome decisões com base em uma condição.

# O bloco if é o bloco condicional mais simples. Ele executa um bloco de código se uma condição for verdadeira.
# Exemplos:

a = 2
if (a == 2):
  print("a é igual a 2")
  # O bloco if verifica se a é igual a 2. Se for, ele imprime "a é igual a 2"

# Importante: o bloco de código que será executado se a condição for verdadeira deve estar indentado. Em Python, a indentação é feita com 2 ou 4 espaços.
# Identação são os recuos que você dá no código. No exemplo acima, o print está recuado em 2 espaços. Isso é importante para o Python entender que o print
# está dentro do bloco if.
# A identação é feita em várias partes do código, como loops, funções, classes e etc, e que serão abordados em outros módulos.

# Agora vamos verificar um exemplo onde a condição é falsa:

a = 3
if (a == 2):
  print("a é igual a 2")
  # O bloco if verifica se a é igual a 2. Se for, ele imprime "a é igual a 2"
  # Como a condição a == 2 é falsa, o bloco de código não será executado.



# O bloco if pode ser seguido por um bloco else. O bloco else é executado se a condição do bloco if for falsa.

a = 3
if (a == 2):
  print("a é igual a 2")
else:
  print("a é diferente de 2")
  # O bloco if verifica se a é igual a 2. Se for, ele imprime "a é igual a 2"
  # Como a condição a == 2 é falsa, o bloco de código dentro do else será executado.

# Teste você mesmo!
a = int(input("Digite um número: "))
if (a == 2):
  print("a é igual a 2")
else:
  print("a é diferente de 2")