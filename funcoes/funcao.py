# Funções são trechos de código usados para 
# repetir determinada ação ao longo do seu código.
# Elas podem receber valores para parâmetros (argumentos) 
# e retornar um valor específico.


def imprime_msg(x, y, z):
    #QUALQUER LÓGICA
    print(x, y , z)

n1 = 1
n2 = 2
n3 = 3
#Exemplo de argumentos nomeados
imprime_msg(1, z=n3, y=n2)

#Exemplo de argumentos não nomeados
imprime_msg(n3, n2, n1)