#Exercício Python 104

print()


#programa principal

def leiaint(msg):
      valor = 0
      while True:
            n = input(msg)
            if n.isnumeric():
                  valor = int(n)
                  break
            else:
                  print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
      return valor

n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o número {n}')

print()