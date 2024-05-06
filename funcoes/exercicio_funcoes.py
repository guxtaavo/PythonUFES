# Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo: 127 -> 721.

def inverte_o_numero(numero):
    return numero[::-1]

numero = input('Digite um número inteiro: ')
print(inverte_o_numero(numero=numero))