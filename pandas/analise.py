import pandas as pd

# Criar um DataFrame de exemplo
data = {
    'Nome': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Idade': [24, None, 22, 23, None],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', None, 'Porto Alegre']
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Exibir o DataFrame original
print("DataFrame Original:")
print(df)
print("\n")

# 1. Identificar dados faltantes
print("Dados faltantes em cada coluna:")
print(df.isnull().sum())
print("\n")

# 2. Remover linhas com dados faltantes
df_sem_na = df.dropna()
print("DataFrame sem linhas com dados faltantes:")
print(df_sem_na)
print("\n")

# 3. Preencher dados faltantes com um valor específico
df_preenchido = df.fillna({'Nome': 'Desconhecido', 'Idade': 0, 'Cidade': 'Indefinida'})
print("DataFrame com dados faltantes preenchidos:")
print(df_preenchido)
print("\n")

# 4. Substituir valores específicos
df_substituido = df.replace({'São Paulo': 'SP', 'Rio de Janeiro': 'RJ'})
print("DataFrame com valores substituídos:")
print(df_substituido)
print("\n")

# 5. Preencher dados faltantes com o valor anterior (forward fill)
df_ffill = df.fillna(method='ffill')
print("DataFrame com forward fill:")
print(df_ffill)
print("\n")

# 6. Preencher dados faltantes com o valor seguinte (backward fill)
df_bfill = df.fillna(method='bfill')
print("DataFrame com backward fill:")
print(df_bfill)
print("\n")

# 7. Preencher dados faltantes com a média (apenas para colunas numéricas)
df['Idade'] = df['Idade'].fillna(df['Idade'].mean())
print("DataFrame com valores numéricos faltantes preenchidos com a média:")
print(df)
print("\n")
