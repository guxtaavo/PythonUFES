# Utilização de pandas com matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Para pegar o caminho da pasta
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_DATA_EXCEL = CAMINHO_RAIZ / 'data.xlsx'

df = pd.read_excel(CAMINHO_DATA_EXCEL)

 # Plotando o gráfico
# plt.figure(figsize=(10, 6))
plt.bar(df['Produto'], df['Quantidade'], color='skyblue')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.title('Quantidade de Produtos Vendidos')
plt.show()