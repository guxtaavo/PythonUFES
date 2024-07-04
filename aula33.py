import numpy as np

# Vetores e Seus Métodos

# Criar um Vetor (Array):
v = np.array([1, 2]) # Podemos passar listas ou tuplas
print(v,type(v))

# Dimensão e Formato:
escalar = np.array(11)
matriz = np.array([[1,2],[3,4]])
print(escalar)
print(matriz)
print(escalar.ndim,v.ndim,matriz.ndim)
print(v.shape,matriz.shape,escalar.shape)
v_2 = matriz.reshape(4,)
print(v_2)
print(matriz.reshape(4,1))

# Indexação:
print(v[0],matriz[0,0:2])

# Copiar Vetores:
u = v.copy()
w = v.view()
v[0] = 3
print(u,w) 

# Iteração:
for x in matriz:
    print(x)
for x in np.nditer(matriz):
    print(x)

# Agrupar e Separar:
print(np.concatenate((matriz, matriz),axis=1))
print(np.stack((matriz, matriz))) # Aumenta uma dimensão
v_3 = np.concatenate((u,w))
arrays = np.array_split(v_3, 2)
print(v_3,arrays[0])

# Buscar, Organizar e Filtrar:
print(np.where(v_3==2)[0])
print(np.sort(v_3))
filtro = (v_3 % 2 != 0) # Apenas ímpares
v_4 = v_3[filtro]
print(filtro,v_4)
