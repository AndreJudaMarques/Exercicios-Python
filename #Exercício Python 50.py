#Exercício Python 50: Desenvolva um programa que leia seis números inteiros
#  e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

print()

soma = 0

for i  in range(1, 7):
      num = int(input('Digite um numero: '))
      if num % 2 == 0:
            soma = soma + num

print(f'O resultados dos numeros pares digitados é de: {soma}' )

print()