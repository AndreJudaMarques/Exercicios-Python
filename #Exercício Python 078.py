#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print()

cont = 0

list = []

for num in range(0,5):
      n = int(input(f'Digite um número para a posição {num + 1}: '))
      list.append(n)
      cont += 1

print(f'Você digitou os valores {list}')
print(f'O maior valor digitado foi o {max(list)} nas posições {list.index(max(list))+1}')
print(f'O menor valor digitado foi o {min(list)} nas posições {list.index(min(list))+1}')

print()
