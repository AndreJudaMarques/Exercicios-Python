#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na tupla.

print()

from random import randint

numeros = []

cont = 0

while cont < 5:
      rand = randint(0,9)
      numeros.append(rand)
      cont += 1

print(numeros)
print(f'O maior = {max(numeros)}')
print(f'O menor = {min(numeros)}')

print()