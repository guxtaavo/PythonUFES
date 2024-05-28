import matplotlib.pyplot as plt

# Dados para o gráfico de barras
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [23, 45, 56, 78, 33]

# Criando o gráfico de barras
plt.bar(categorias, valores)

# Adicionando rótulos aos eixos e título ao gráfico
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

# Exibindo o gráfico
plt.show()
