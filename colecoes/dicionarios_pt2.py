# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries


# lista = ['Gustavo', 20, 'UFES', 'ES']
pessoa = {
    "nome":"Gustavo Nunes",
    "idade":20,
    "instituicao":'UFES',
    "endereco":[
        'Rua alguma coisa', 'Rua outra coisa'
    ]
}

# Método GET -> retorna o valor da chave, pode passar um valor caso não encontre
print(pessoa.get('nome', 'pode passar algo aqui opcional, por padrão = None'))

# Método KEYS -> retorna as chaves do dict
print(pessoa.keys())

# Método VALUES -> retorna as valores do dict
print(pessoa.values())

# Método clear -> Limpa o conteúdo do dict
pessoa.clear()

# Método items -> Retorna o conjunto de chave e valor do dict em forma de tupla
print(pessoa.items())