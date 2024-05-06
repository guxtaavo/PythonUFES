# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
# a multiplicação e os números.

vetor = input('Digite um vetor, utilizando "espaços" para separar o número: ')
vetor = vetor.split()
print(vetor)

for i in range(len(vetor)):
    vetor[i] = int(vetor[i])

soma = 0
multiplicao = 1

for numero in vetor:
    soma += numero

for numero in vetor:
    multiplicao *= numero

print(soma, multiplicao)