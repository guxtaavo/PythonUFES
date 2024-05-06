# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
#


# lista = ['Gustavo', 20, 'UFES', 'ES']
pessoa = {
    "nome":"Gustavo Nunes",
    "idade":20,
    "instituicao":'UFES',
    "endereco":[
        'Rua alguma coisa', 'Rua outra coisa'
    ]
}

pessoa.pop("nome")
print(pessoa)

