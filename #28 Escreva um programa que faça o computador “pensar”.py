 #28: Escreva um programa que faça o computador “pensar” 
#em um número inteiro entre 0 e 5 
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

from time import sleep
from random import randrange

print()

print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
n = randrange(6) #até o 5
sleep(0.5)
numero = int(input('Em que número estou pensando? '))
print('Processando')
sleep(2)
if numero == n:
      print(f'PARABÉNS!!! Você acertou meu número!')
else:
      print(f'GANHEI!!! Eu pensei no número {n} e não no {numero}!')
print('-=-' * 10)

print()