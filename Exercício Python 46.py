#Exercício Python 46

# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva 
# para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print()

for numero in range(10, -1, -1):
      print(numero)
      sleep (0.5)
print('Bum! Bum! Bum! ')


print()