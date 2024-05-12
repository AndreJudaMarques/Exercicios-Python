#Exercício Python 103

print()

def ficha(jog='<desconhecido>' , gol=0):
      print(f'O jogador {jog} fez {gol} gols no campeonato.')


#programa principal
n = input('Nome do jogador: ')
g = input('Numero de gols: ')
if g.isnumeric():
      g = int(g)
else:
      g = 0
if n.strip() == '':
      ficha(gol=g)
else:
      ficha(n, g)

print()