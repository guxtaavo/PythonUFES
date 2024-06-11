# DataFrame

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50.0, 40, 45],
    "fruta": ["Banana", "Apple", "Grape"]
}

df = pd.DataFrame(data)
# print(df)

# Nomeando os índices
df2 = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df2)
print(df2.loc['day2'])

# Trabalhando com análises estatísticas em dataframe
mean = df2['calories'].mean()
print(f'Média: {mean:.2f}')
