# Gráficos de linha

import matplotlib.pyplot as plt

# Plotar gráfico só com o valor de Y
plt.plot([1, 2, 3, 4]) 
#       x = 0  1  2  3     

# Passando eixo X e eixo Y
plt.plot([1, 4], [1, 16]) # Associação ponto a ponto
plt.axis((0, 6, 0, 20)) # Intervalo dos eixos

# Múltiplas Linhas
linha1 = [3, 8, 1, 10]
linha2 = [6, 2, 7, 11]

plt.plot(linha1)
plt.plot(linha2)

# Múltiplos Gráficos
fig = plt.figure(figsize=[14,7])
gráfico1 = fig.add_subplot(1,2,1)
gráfico2 = fig.add_subplot(1,2,2)
gráfico1.plot(linha1)
gráfico2.plot(linha2)

plt.show()
