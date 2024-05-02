# Variáveis são utilizadas para armazenar alguma informação
# Tipo não fixo 
# Restrições (Números no começo, caracteres especiais e palavras reservadas)
# Case-sensitive 
# Declaração múltipla de variáveis
# Por padrão em python, utilizamos snake_case
# Utilizar nomes adequados

# Ao operarmos com variáveis, o resultado se torna mais flexivel
x = 30
soma = x + 10
print(soma)

# Podemos alterar o tipo da variável, por exemplo, x era int e agora é str
x = "Yago"
print(x)

# Só podemos utilizar letras, números e underline nos nomes das variáveis
idade_yago = 21 # snake_case: todas as letras minúsculas, com as palavras separadas por underline

# Como o if é uma palavra reservada em python, não podemos utilizá-la como o nome de uma variável
# if = "Yago"
# print(if)

# Case sensitive: Letras maiúsculas e minúsculas geram variáveis distintas
IDADE_YAGO = 30
print(idade_yago,IDADE_YAGO)

# Utilizamos vírgula para declarar múltiplas variáveis, que são atribuidas na mesma ordem que são declaradas
nome,idade = "gustavo",21
print(nome,idade)
