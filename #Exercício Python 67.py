#Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
#  um de cada vez, para cada valor digitado pelo usuário.
#  O programa será interrompido quando o número solicitado for negativo.

print()

n = 0
c = 1

while True:
      n = int(input('Quer ver a tabuada de qual valor? [negativo para parar] '))
      print('---' * 10)
      if n < 0:
            break
      while c <= 10:
            print(f'{n} x {c} = {n * c}')
            c += 1
      c = 1

print('Programa encerrado.')

print()