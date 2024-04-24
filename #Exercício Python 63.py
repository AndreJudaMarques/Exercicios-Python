#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print()

print('---' * 15)
print(' Sequência de Fibonacci ')
print('---' * 15)

numero = int(input('Quantos termos você quer mostrar? '))
print('~~~' * 15)

n1 = 0
n2 = 1
###### 0   1 / 1   1 / 2   3 / 5   8 / 13   21 / 

print(n1, end=' -> ')
print(n2, end=' -> ')
cont = 2
while cont < numero:
      fibo = n1 + n2
      n1 = n2
      n2 = fibo
      print(fibo, end=' -> ')
      cont += 1
print('FIM')
print('~~~' * 15)


print()