# Mais métodos para análise de dados

import pandas as pd
from pathlib import Path

# Para pegar o caminho da pasta
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_DATA_CSV = CAMINHO_RAIZ / 'data.csv'

df = pd.read_csv(CAMINHO_DATA_CSV)

# Para pegar as linhas sem ser a primeira e a última
print(df.head())
# Diferente da utilização do:
pd.options.display.max_rows = 2
print(df)

# Pega as linhas do final para o início, por padrão, 5 também igual o head
print(df.tail())

# Para pegar informações da coluna
print(df.info())