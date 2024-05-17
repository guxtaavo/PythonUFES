# Gráficos de linha

import matplotlib.pyplot as plt

# Plotar gráfico só com o valor de Y
# plt.plot([1, 2, 3, 4]) 
#       x = 0  1  2  3     
# plt.show()

# Passando eixo X e eixo Y
plt.plot([1, 4], [1, 16]) # Associação ponto a ponto
plt.axis((0, 6, 0, 20)) # Intervalo dos eixos
plt.show()
