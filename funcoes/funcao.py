# Funções são trechos de código usados para 
# repetir determinada ação ao longo do seu código.
# Elas podem receber valores para parâmetros (argumentos) 
# e retornar um valor específico.


def imprime_msg(x, y, z):
    #QUALQUER LÓGICA
    print(x, y , z)

    # As váriaveis dentro da função, só existem dentro dela, e não existem no escopo geral do código, são váriaveis temporarias
    # Só irão existir enquanto o código estiver no escopo da função


    # A função pode retornar algo, que voce armazenaria em alguma variavel ou utilizaria em alguma coisa
    # Ou não precisa retornar nada
    # Pode retornar uma outra função também, dependendo da sua lógica dentro do código
    # return

n1 = 1
n2 = 2
n3 = 3

#Exemplo de argumentos nomeados
imprime_msg(1, z=n3, y=n2)

#Exemplo de argumentos não nomeados
imprime_msg(n3, n2, n1)