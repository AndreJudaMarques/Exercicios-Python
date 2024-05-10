#Exercício Python 100

from random import randint

print()

def rands():
      lista = []
      print('Sorteando 5 valores da lista:', end=' ')
      cont = 0
      while cont < 5:
            rand = randint(0,9)
            if rand not in lista:
                  lista.append(rand)
                  print(rand, end=' ')
                  cont += 1
            else:
                  rand = randint(0,9)
      print('Pronto!')
      pares = 0
      for i in lista:
            if i % 2 == 0:
                  pares += i
      print(f'Somando os valores pares de {lista}, temos {pares}')

rands()            

print()