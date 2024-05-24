# Crie um programa que trace o gráfico de uma função linear a partir dos coeficientes de y = ax + b
# e mostre qual é a função no título do gráfico

import matplotlib.pyplot as plt

print("Digite os coeficientes de uma função linear y = ax + b:\n")
a = float(input("a: "))
b = float(input("b: "))

if not a == 0:
    plt.plot([0, -b/a], [b, 0]) # (0,b) (-b/a,0)
else:
    plt.plot([0, 5], [b, b],color = 'black')
plt.title(f"y = {a}x + {b}") 
plt.xlabel(f"x") 
plt.ylabel(f"y")
plt.show()
