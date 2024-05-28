import matplotlib.pyplot as plt

# Dados para o gráfico de pizza
tamanhos = [25, 30, 15, 10, 20]
labels = ['Maçã', 'Banana', 'Laranja', 'Pera', 'Uva']

# Criando o gráfico de pizza
plt.pie(tamanhos, labels=labels, autopct='%1.1f%%')

# Adicionando título ao gráfico
plt.title('Gráfico de Pizza')

# Garantindo que o gráfico seja desenhado como um círculo
plt.axis('equal')

# Exibindo o gráfico
plt.show()
