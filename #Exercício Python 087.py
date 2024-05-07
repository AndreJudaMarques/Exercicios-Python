#Exercício Python 087
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

print()

matriz = [[],[],[],
          [],[],[],
          [],[],[]]

soma = 0
segunda = 0
for i in range(0,9):
      matriz[i] = int(input('Digite um numero: '))
      if i % 2 ==0:
            soma += i    
for i in matriz:
      if i == 3:
            segunda += i
      elif i == 4:
            segunda += i
      elif i == 5:
            segunda += i
print(f'{' '}')
for i in matriz:
      print(f'{i:^5}', end=' ')
      if i == 3:
            print(f'\n{i:^5}')
      elif i == 6:
            print(f'\n{i:^5}')
print(f'{' '}')
print(f'A soma dos valores pares é de {soma}')
print(f'A soma dos valores da terceira linha é {segunda}')

print()

# print(f'{matriz[:3]}')
# print(f'\n{matriz[3:6]}')
# print(f'\n{matriz[6:]}')