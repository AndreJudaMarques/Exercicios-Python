#Exercício Python 096

print()

print('Controle de terrenos')
print('---' * 7)

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

def area(larg, comp):
      total = larg * comp
      print(f'A área de um terreno {larg} x {comp} é de {total}m². ')

area(larg, comp)

print()