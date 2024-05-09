#Exercício Python 095: Aprimore o desafio 93

print()

dados = {}

while True:
      dados['nome'] = nome = input('Nome do jogador: ')
      quantas = int(input(f'Quantas partidas {nome} jogou? '))

      gol = []
      tot = 0
      for i in range(0, quantas):
            goll= int(input(f'Quantos gols na partida {i+1}: '))
            tot += goll
            gol.append(goll)

      while True:
            resp = input('Quer continuar? [S/N]: ').upper()[0]
            if resp in 'SN':
                  break
            print('ERRO! Responda apenas S ou N.')
      if resp == 'N':
            break

print('-=-' * 15)

dados['gols'] = gol
dados['total'] = tot

print(dados)
print('-=-' * 15)

for key, value in dados.items():
      print(f'O campo {key} tem o valor {value}')
print('-=-' * 15)

print(f'O jogador {nome} jogou {quantas} partidas.')
for contagem, i in enumerate(gol):
      print(f'=> Na partida {contagem + 1}, fez {i} gols.')

print(f'Foi um total de {tot} gols.')
print('-=-' * 15)
print()