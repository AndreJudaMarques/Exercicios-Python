#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

print()

llist = []
maior = 0
menor = 2000

while True:
      nome = input('Nome: ')    
      peso = float(input('Peso: '))
      if peso > maior:
            maior = peso
      else:
            if peso < menor:
                  menor = peso
      llist.append([nome, peso])
      cont = input('Quer continuar? [S/N]: ').strip()
      if cont in 'nN':
            break

print(llist)
print(f'Ao todo, você cadastou {len(llist)} pessoas')      
print(f'O maior peso foi de {maior:.1f}kg. Peso de ', end='')
for p in llist:
      if p[1] == maior:
            print(f'{p[0]}',end=' ')
print(f'\nO menor peso foi de {menor:.1f}kg. Peso de ', end='')
for p in llist:
      if p[1] == menor:
            print(f'{p[0]}',end=' ')

print('\n')

# llist = [['Ana', 75.5], ['Pedro', 89]]
# print(llist[0][1])