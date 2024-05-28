import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dados para o gráfico 3D
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Criando a figura e os eixos 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotando a superfície 3D
ax.plot_surface(x, y, z, cmap='viridis')

# Adicionando rótulos aos eixos e título ao gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfico 3D')

# Exibindo o gráfico
plt.show()
