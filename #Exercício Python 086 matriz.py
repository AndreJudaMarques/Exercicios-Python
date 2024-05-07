#Exercício Python 086 matriz


print()

matriz = [[],[],[],  # linha 0
          [],[],[],  # linha 1
          [],[],[]]  # linha 2

      #print(len(matriz)) = 9

#matriz[0].append(1)

for i in range(0,9):
      n = int(input(f'Digite um valor para : '))
      matriz[i].append(n)

print(f'{matriz[:3]}')
print(f'\n{matriz[3:6]}')
print(f'\n{matriz[6:]}')


print()

# matriz = [[0,0],[0,1],[0,2],  # linha 0
#           [],[],[],  # linha 1
#           [],[],[]]   #linha 2