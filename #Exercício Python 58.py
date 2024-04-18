#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o 
#computador vai “pensar” em um número entre 0 e 10.

from time import sleep
from random import randint

print()

print('Sou seu computador...')
sleep(0.5)

n = randint(1,10) #rodando aleatorios de 1 a 10, check

print('Acabei de pensar em um numero entre 0 e 10.')
sleep(0.5)
print('Será que você consegue adivinhar? ')
sleep(0.3)

numero = int(input('Qual seu palpite? '))

tentativas = 1
while numero != n:
      tentativas += 1
      if numero < n:
            print('Mais... tente mais uma vez.')
            numero = int(input('Qual seu palpite? '))
      else:
            print('Menos... tente mais uma vez.')
            numero = int(input('Qual seu palpite? '))

print(f'Acertou! com {tentativas} tentativas. Parabéns! ')
print(f'O número que pensei foi {n} e digitado foi {numero}')


print()