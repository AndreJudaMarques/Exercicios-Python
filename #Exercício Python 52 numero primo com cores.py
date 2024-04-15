#Exercício Python 52: Faça um programa que leia um número inteiro 
#e diga se ele é ou não um número primo.

print()

numero = int(input('Digite um numero: '))

total = 0

for c in range(1, numero + 1):
      if numero % c == 0:
            print(f'\033[33m{c}', end=' ')
            total += 1
      else:
            print(f'\033[31m{c}', end=' ')

print(f'\n\033[mO {c} foi dividido {total} vezes')
if total == 2:
      print('E por isso ele é PRIMO.')
else:
      print('E por isso ele NÃO é PRIMO.')
print(' ')