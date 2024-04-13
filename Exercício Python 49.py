#Exercício Python 49

# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

print()

numero = int(input('Digite o número que gostaria de fazer a TABUADA: '))

print(f'Tabuada do {numero}: ')

for num in range(1, 11):
      print(f'{num} x {numero} = {num * numero}')

print()