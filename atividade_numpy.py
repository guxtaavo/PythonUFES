import numpy as np
import matplotlib.pyplot as plt

# Crie um programa que trace o gráfico da função seno de 0 a 360° utilizando matplotlib
# Dica: Pegue intervalos curtos entre os ângulos

angulos = []
senos = []
for angulo in range(0,360,1):
    angulos.append(angulo)
    angulo = np.deg2rad(angulo)
    senos.append(np.sin(angulo))

plt.title("y = sen(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(angulos,senos,color='black')
plt.show()
