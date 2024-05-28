# Lendo arquivo csv com o Pandas

import pandas as pd
from pathlib import Path

# Para pegar o caminho da pasta
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_DATA_CSV = CAMINHO_RAIZ / 'data.csv'

# Para definir o max de linhas 
# pd.options.display.max_rows = 2

# Criando um DataFrame a partir de um arquivo csv
df = pd.read_csv(CAMINHO_DATA_CSV)
print(df) 

# Para tratar itens duplicados
# df = df.drop_duplicates(keep='last')
df = df.drop_duplicates(['Produto'])
# print(df)

# Para apagar linha ou coluna
# df = df.drop('Produto', axis='columns')
df = df.drop(1, axis='index')
print(df)