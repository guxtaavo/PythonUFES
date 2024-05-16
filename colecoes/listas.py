# Listas em Python
# https://docs.python.org/pt-br/3/tutorial/datastructures.html
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Métodos úteis: append, insert, pop, clear, extend, +

# lista = [['qa', True], [123]]
# #              0          1  
# print(type(lista[0][1]))

# APPEND - adiciona o elemento no final da lista
# lista = [1, 2, 3]
# lista.append(4)
# print(lista)

# INSERT - adiciona um elemento na lista, mas você pode escolher o local que ele vai ser inserido
# lista = [1, 2, 3]
# lista.insert(0, 0)
# print(lista)

# POP - elimina o último elemento por padrão, mas você pode escolher o indice que vai ser eliminado
# lista = [1, 2, 3]
# lista.pop(0)
# print(lista)

# CLEAR - limpa a lista, mas não exclui a váriavel!
# lista = [1, 2, 3]
# lista.clear()
# print(lista)

# EXTEND - adiciona/'concatena' uma lista na outra
# lista = [1, 2, 3]
# lista_2 = [4, 5]
# lista.extend(lista_2)
# print(lista)

# SORT - ordena a lista do menor para o maior por padrão
# lista = [1, 3, 0, 2]
# lista.sort()
# print(lista)

# REVERSE - inverte a ordem da lista
# lista = [1, 2, 2, 34]
# lista.reverse()
# print(lista)

# COPY - copia os dados da lista para uma nova lista (CRIA UMA NOVA LISTA, NÃO APONTA PARA O MESMO LADO!!!)
lista = [1, 2, 3]
lista_nova = lista.copy()
lista_nova[1] = 10
print(lista)
# Se você igualar a lista, você só vai estar apontando para o mesmo endereço, e não criando uma nova lista. Observe:
lista = [1, 2, 3]
lista2 = lista
lista2[2] = 14 #Estou alterando o valor da lista2, porém vai alterar a lista também, observe no print a seguir:
print(lista[2])

# COUNT - conta a quantidade de vezes que apareceu na lista
# lista = [1, 2, 3, 3, 0]
# print(lista.count(3))


