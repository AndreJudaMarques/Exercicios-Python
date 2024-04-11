#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

print()
print('-=-' * 10)
print(f'JOKENPÔ! Contra o PC')
print('-=-' * 10)

from time import sleep
from random import randint

computador = randint(1,3)
jogo = ['PEDRA', 'PAPEL', 'TESOURA']
escolhaPC = jogo[computador - 1]

#print(escolhaPC)

#print(computador)

print('Sua Jogada! ')

print(f'''[1] PEDRA
      \n[2] PAPEL
      \n[3] TESOURO ''')
print()

jogada = int(input('Qual a sua jogada: '))
print()

if jogada in [1, 2, 3]:
      sleep(0.5)
      print('JÓ!')
      sleep(0.5)
      print('KEN!')
      sleep(0.5)
      print('PÔ!')
      print('-=-' * 10)
      print(f'Computador jogou {escolhaPC}')
      if jogada == 1:
            print(f'Jogador jogou PEDRA')
      elif jogada == 2:
            print(f'Jogador jogou PAPEL')
      elif jogada == 3:
            print(f'Jogador jogou TESOURA')
      print('-=-' * 10)
      print()
      if computador == jogada:
            print('EMPATE')
      else:
            if computador == 1 and jogada == 2:
                  print('''Jogador Venceu! 
                        \npois PAPEL VENCE PEDRA''')
            elif computador == 1 and jogada == 3:
                  print('''Computador Venceu! 
                        \npois PEDRA VENCE TESOURA''')
            elif computador == 2 and jogada == 1:
                  print('''Computador Venceu! 
                        \npois PAPEL VENCE PEDRA''')
            elif computador == 2 and jogada == 3:
                  print('''Jogador Venceu! 
                        \npois TESOURA VENCE PAPEL''')
            elif computador == 3 and jogada == 1:
                  print('''Jogador Venceu! 
                        \npois PEDRA VENCE TESOURA''')
            elif computador == 3 and jogada == 2:
                  print('''Computador Venceu! 
                        \npois TESOURA VENCE PAPEL''')
else:
      print('Opção inválida')

print()