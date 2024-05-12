#Exercício Python 102

print()

#funcao
def fatorial(n, show= False):
      from time import sleep
      f = 1
      for c in range(n, 0, -1):
            if show:
                  print(c, end=' ')
                  sleep(0.3)
                  if c > 1:
                        print(f'x ', end=' ')
                  else:
                        print(' = ', end=' ')
            f*=c
      sleep(0.3)
      return f


#programa principal
print(fatorial(5, show=True))
print(fatorial(5, show=False))

print()