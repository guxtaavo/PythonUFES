# Escopo de variáveis

# Variável global: é definida fora de qualquer função e pode ser acessada 
# em qualquer parte do código.
global_var = "global"

def escopo_variavel():
    # Variável local: é definida dentro de uma função e só pode ser
    # acessada dentro dessa função.
    local_var = "local"
    print(local_var)  # Isso funciona
    print(global_var)  # Variáveis globais podem ser acessadas dentro de funções

# Chamando a função para mostrar o escopo local
escopo_variavel()

# Tentando acessar a variável local fora da função (vai gerar um erro)
# print(local_var)  # Isso não funciona, pois local_var é local 
# à função escopo_local