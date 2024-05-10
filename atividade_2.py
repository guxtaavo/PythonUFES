# 1- Escreva um código Python que peça ao usuário um número e imprima na tela se o número é par ou ímpar.

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 2- Escreva um código Python que leia dois números do usuário e imprima na tela o maior deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
    print("O maior número é o primeiro.")
elif numero2 < numero1:
    print("O maior número é o segundo.")
else:
    print("Os números são iguais.")

# 3- Escreva um código Python que leia três números do usuário e imprima na tela o menor deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
menor = num1

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print ("O menor número é", menor)


# 4- Escreva um código Python que calcule a média de três números digitados pelo usuário.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
media = (numero1 + numero2 + numero3) / 3
print("A média dos números é", media)

# 5- Escreva um código Python que imprima na tela os números de 1 a 101, pulando de 2 em 2.
for i in range(1, 102, 2):
    print(i)

# 6- Escreva um código Python que use a instrução if para verificar se um número digitado pelo usuário é positivo, negativo ou zero.
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 7- Escreva um código Python que use a instrução while para pedir ao usuário um número até que ele digite um número maior que 10.
numero = 0
while numero <= 10:
    numero = int(input("Digite um número: "))

# 8- Escreva um código Python percorra uma lista de carros e imprima na tela o nome de um carro específico que o usuário digitar, caso ele exista na lista.
carros = ["Fusca", "Gol", "Celta", "Palio", "Uno", "Onix", "HB20", "Civic", "Corolla", "Cruze"]

nomeDoCarro = input("Digite um carro: ")
carroExiste = False

for carro in carros:
    if carro == nomeDoCarro:
        print(carro)
        carroExiste = True

if not carroExiste:
    print("Carro inválido!")