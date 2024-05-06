#Exercício Python 085



print()

numeros = [[],[]] #print(numeros[0]) = ['p']

for i in range (0,7):
      n = int(input(f'Digite o {i+1}º valor: '))
      if n % 2 == 0:
            numeros[0].append(n)
      else:
            numeros[1].append(n)
print('')

print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')
print('')