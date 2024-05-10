# Ainda podemos utilizar o elif, que é uma abreviação de else if, que é utilizado para verificar mais de uma condição.

a = int(input("Digite um número: "))
if (a == 2):
  print("a é igual a 2")
elif (a == 3):
  print("a é igual a 3")
else:
  print("a é diferente de 2 e 3")
# O que esse código simplesmente faz é duas verificações: se a é igual a 2 e se a é igual a 3. Se a for igual a 2, ele imprime "a é igual a 2".
# Se a for igual a 3, ele imprime "a é igual a 3". Se a não for igual a 2 e 3, ele imprime "a é diferente de 2 e 3".


# Podemos fazer quantos elifs quisermos. Por exemplo:
a = int(input("Digite um número: "))
if (a == 2):
  print("a é igual a 2")
elif (a == 3):
  print("a é igual a 3")
elif (a == 4):
  print("a é igual a 4")
elif (a == 5):
  print("a é igual a 5")
else:
  print("a é diferente de 2, 3, 4 e 5")