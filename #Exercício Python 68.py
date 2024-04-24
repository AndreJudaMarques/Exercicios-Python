#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

print()

from random import randint

print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 10)

cont = 0
while True:
      r = randint(1,11) # 1 ou 2 random
      n = int(input('Diga um valor: '))
      parimpar = input('Par ou Ímpar? [P/I]: ').lower().strip()
      print('---' * 15)
      total = n + r
      if n % 2 != 0 and parimpar in 'pP':
            print('Você PERDEU! ')
            break
      elif n % 2 == 0 and parimpar in 'iI':
            print('Você PERDEU! ')
            break
      else:
            print('Você VENCEU! ')
            cont += 1
            print('vamos jogar novamente...')

print(f'GAME OVER! Você venceu {cont}')
print()
