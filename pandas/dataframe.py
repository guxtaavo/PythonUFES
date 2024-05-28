# DataFrame

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

# Pode pegar dados de um par de índices específicos
print(df.loc[0])

# Pode-se nomear os índices
df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df2) 
print(df2.loc["day1"])
