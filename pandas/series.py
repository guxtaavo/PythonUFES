# Séries

import pandas as pd

# Séries simples de array
obj = pd.Series([4, 7, -5, 3])
print(obj)

# Séries com índice
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a',
'e']) 
#print(obj2)
print(obj2['e'])

# Podemos usar o tipo bool
if 'a' in obj2:
    print('Contém index "A"')
else:
    print('Não contém index "A"')

# Pode-se criar uma série a partir de um dict
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon':
16000, 'Utah' : 5000.0} 
obj3 = pd.Series(sdata)
print(obj3)

# Exemplo de análises estátisticas
# Criando uma série de exemplo
dados = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculando várias estatísticas
media = dados.mean()
mediana = dados.median()
desvio_padrao = dados.std()
variancia = dados.var()
minimo = dados.min()
maximo = dados.max()
soma = dados.sum()
contagem = dados.count()
primeiro_quartil = dados.quantile(0.25)
terceiro_quartil = dados.quantile(0.75)

# Exibindo os resultados
print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio_padrao)
print("Variância:", variancia)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Soma:", soma)
print("Contagem:", contagem)
print("Primeiro Quartil (25%):", primeiro_quartil)
print("Terceiro Quartil (75%):", terceiro_quartil)