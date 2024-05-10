#Exercício Python 099

from time import sleep

print()

def linha():
      print('-=-' * 12)

def maior(*n):
      linha()      
      print('Analisando os valores passados...')
      for num in n:
            print(f'{num}', end=' ', flush=True)
            sleep(0.3)
      print(f'Foram informados {len(n)} ao todo.')
      if len(n) == 0:
            print('O maior valor informado foi nenhum')
      else:
            print(f'O maior valor informado foi {max(n)}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

print()