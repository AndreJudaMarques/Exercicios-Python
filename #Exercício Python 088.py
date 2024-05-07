#Exercício Python 088

from random import randrange
from time import sleep

print()

print('---' * 15)
print(f'{"Jogos na MEGA SENA":^45}')
print('---' * 15)

lista = []
jogos = []

qnt = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-' * 2, f'{f"SORTEANDO {qnt} JOGOS":^30}', '-=-' * 2)

cont = 0
n = 0
while cont < qnt:
      while n < 6:
            numeros = randrange(1,60)
            if numeros not in lista:
                  lista.append(numeros)
            n += 1
      cont += 1
      n = 0
      lista.sort() 
      jogos.append(lista[:])
      lista.clear()
sleep(1)
for indice, listax in enumerate(jogos):
      print(f'Jogo {indice + 1}: {listax}')
      sleep(0.5)
      
print(lista)
print(jogos)

print()

