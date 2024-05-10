# O while loop é uma estrutura de controle que permite que você repita um bloco de código enquanto uma condição for verdadeira.

# Exemplo:
# Vamos definir um while loop que imprime "Olá, mundo!" 5 vezes.
i = 0
while i < 5:
  print("Olá, mundo!")
  i += 1
# Basicamente o que esse código faz é definir uma variável i que será usada para controlar o número de vezes que o bloco de código será executado.
# Perceba que i é incrementado a cada iteração do loop. Se não fizermos isso, o loop será infinito, pois a condição i < 5 sempre será verdadeira.

# Teste você mesmo!
i = 0
loop = int(input("Digite um número: "))
while i < loop:
  print(i)
  i += 1
# O que esse código faz é definir uma variável i que será usada para controlar o número de vezes que o bloco de código será executado.
# O usuário define o valor de loop e o loop imprime os números de 0 até loop - 1.

# Outra utilidade do while loop é criar um loop infinito. Por exemplo:
while True:
  print("Loop infinito!")
  # O que esse código faz é criar um loop infinito que imprime "Loop infinito!". Para parar esse loop, você pode pressionar Ctrl + C no terminal.
  # Esse tipo de loop é útil para criar programas que ficam rodando indefinidamente, como servidores e etc.