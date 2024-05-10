# O for loop é uma estrutura de controle que permite que você repita um bloco de código várias vezes.

# Exemplo:
# Vamos definir um for loop que imprime "Olá, mundo!" 5 vezes.
for i in range(5):
  print("Olá, mundo!")
# Basicamente o que esse código faz é definir uma variável i que será usada para controlar o número de vezes que o bloco de código será executado.
# Nesse caso, estamos definindo que o i irá variar de 0 a 4 (pois o range(5) gera uma sequência de números de 0 a 4).
# Range: Define um intervalo de números. No caso do range(5), ele define um intervalo de 0 a 4.


for i in range(5):
  print(i)
  # O que esse código faz é definir uma variável i que irá variar de 0 a 4 (pois o range(5) gera uma sequência de números de 0 a 4).
  # E ele imprime o valor de i a cada iteração do loop.



# Podemos usar o comando break para interromper o loop. Por exemplo:

for i in range(5):
  if i == 3:
    break
  print(i)
  # O que esse código faz é definir uma variável i que irá variar de 0 a 4 (pois o range(5) gera uma sequência de números de 0 a 4).
  # E ele imprime o valor de i a cada iteração do loop. Mas se i for igual a 3, o loop é interrompido.


# Podemos usar o comando continue para pular uma iteração do loop. Por exemplo:
for i in range(5):
  if i == 3:
    continue
  print(i)
  # O que esse código faz é definir uma variável i que irá variar de 0 a 4 (pois o range(5) gera uma sequência de números de 0 a 4).
  # E ele imprime o valor de i a cada iteração do loop. Mas se i for igual a 3, ele pula essa iteração e vai para a próxima.


# Ainda podemos definir o intervalo do range. Por exemplo:
for i in range(2, 5):
  print(i)
  # O que esse código faz é definir uma variável i que irá variar de 2 a 4 (pois o range(2, 5) gera uma sequência de números de 2 a 4).


# Podemos também definir um intervalo e um incremento. Por exemplo:
for i in range(2, 10, 2):
  print(i)
  # O que esse código faz é definir uma variável i que irá variar de 2 a 9 (pois o range(2, 10, 2) gera uma sequência de números de 2 a 9 com incremento de 2).
  # Basicamente ele "pula" de 2 em 2.



# Outra utilidade é percorrer uma lista com o for loop. Por exemplo:
frutas = ['banana', 'maçã', 'uva', 'melancia']
for fruta in frutas:
  print(fruta)
  # O que esse código faz é percorrer a lista frutas e imprimir cada elemento da lista.


# Teste você mesmo!
loop = int(input("Digite um número: "))
for i in range(loop):
  print(i)
  # O que esse código faz é definir uma variável i que irá variar de 0 a loop (loop que é definido pelo usuário).


