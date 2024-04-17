#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

print()

maior = 0
menor = 1000

for pessoa in range(1,6):
      peso = float(input(f'Peso da {pessoa}º pessoa: '))
      if peso > maior:
            maior = peso
      elif peso < menor:
            menor = peso
print()
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')

print()