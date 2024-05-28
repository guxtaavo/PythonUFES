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