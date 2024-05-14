#Exercício Python 113

#from utilizadescev import dados

def leiaint(msg):
      valor = 0
      while True:
            n = input(msg).strip()
            if n.isnumeric():
                  valor = int(n)
                  break
            else:
                  print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
      return valor

            


print()

nint = leiaint('Digite um numero inteiro: ')
#nreal = dados.leiareal('Digite um numero real: ')

#print(f'O valor inteiro digitado foi {nint} e o real foi {nreal}')



print()