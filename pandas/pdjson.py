# Lendo arquivo json com o Pandas

import pandas as pd
from pathlib import Path

# Para pegar o caminho da pasta
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_DATA_JSON = CAMINHO_RAIZ / 'data.json'

df = pd.read_json(CAMINHO_DATA_JSON)
#pd.read_json
print(df)

# Tratamento de duplicadas
df = df.drop_duplicates(['Produto'], keep='last')
print(df)
