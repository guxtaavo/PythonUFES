import numpy as np

# Função Random e Operações Matemáticas

# Não é possível gerar um número aleatório usando algorítmos
# Função Random:
x = np.random.randint(100) # Inteiro
y = np.random.rand() # Float
print(x,y)
matriz = np.random.randint(100,size=(3,3))
print(matriz)
escolha = np.random.choice([1937, 1968, 2012, 2023])
print(escolha)

# Distribuição de Probabilidade:
escolha = np.random.choice([1937, 1968, 2012, 2023], p = [0.0,0.1,0.3,0.6],size = (10))
print(escolha)

# Permutação:
vetor = np.array([1,2,3,4,5])
vetor_permutado = np.random.permutation(vetor)
print(vetor)
print(vetor_permutado)

# Operações Básicas:
v1 = np.array([1,2])
v2 = np.array([3,4])
soma = np.add(v1,v2)
subtração = np.subtract(v2,v1)
produto = np.multiply(v1,v2)
divisão = np.divide(v2,v1)
potência = np.power(v2,v1)
resto = np.remainder(v2,v1)
print(soma,subtração,produto,divisão,potência,resto)

# Arredondamento:
v = np.array([1.255,3.545])
truncamento = np.trunc(v)
arredondamento = np.around(v)
print(truncamento,arredondamento)

# Operações Avançadas:
escalar = 16
logaritmo = np.log2(escalar) # Bases 2,10 e Natural
print(logaritmo)
angulos = np.array([0,90,180,270])
angulos = np.deg2rad(angulos) # Converte o Ângulo
seno = np.sin(angulos)
print(seno)
senos = np.array([0,1,0,-1])
arcosenos = np.arcsin(senos)
print(arcosenos)
