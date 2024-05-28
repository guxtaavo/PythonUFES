import numpy as np
import matplotlib.pyplot as plt

# Dados para o histograma (amostras aleatórias de uma distribuição normal)
dados = np.random.normal(0, 1, 1000)

# Criando o histograma
plt.hist(dados, bins=30, edgecolor='black')

# Adicionando rótulos aos eixos e título ao gráfico
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')

# Exibindo o gráfico
plt.show()
