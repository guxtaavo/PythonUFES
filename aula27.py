# Gráficos de Dispersão
# https://www.w3schools.com/python/matplotlib_scatter.asp

import matplotlib.pyplot as plt

# x,y = [5,7,8,7,2,17,2,9,4,11,12,9,6],[99,86,87,88,111,86,103,87,94,78,77,85,86]
# colors = ["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"]
# plt.plot(x,y,'ro')
# plt.scatter(x,y,c=colors)

# Parte para fazer com ColorMaps
# É ordenado
x,y = [5,7,8,7,2,17,2,9,4,11,12,9,6],[99,86,87,88,111,86,103,87,94,78,77,85,86]
colors_map = [0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100]
plt.scatter(x,y,c=colors_map, cmap='viridis')
plt.colorbar()
plt.show()
