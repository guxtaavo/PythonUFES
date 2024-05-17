# Marcadores, títulos, tipos de linha e grid
#https://www.w3schools.com/python/matplotlib_markers.asp
#https://www.w3schools.com/python/matplotlib_line.asp

import matplotlib.pyplot as plt

# Marcadores
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], '<') #, 'TIPO DE MARCADOR')
# plt.show()

# Títulos
# font1 = {'family':'arial','color':'blue','size':20}
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.title("Título", fontdict = font1, color='r', loc='right')# Título principal
# plt.xlabel('Eixo') # X ou Y
# plt.show()

# Tipos de linha
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], ls = ":", color = 'r', linewidth='20')
# plt.show()

# Tipo de grid
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()
