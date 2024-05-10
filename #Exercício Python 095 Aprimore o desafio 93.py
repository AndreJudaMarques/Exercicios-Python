#Exercício Python 095: Aprimore o desafio 93

print()

galera = []
dados = {}

while True:
      
      dados['nome'] = nome = input('Nome do jogador: ')
      quantas = int(input(f'Quantas partidas {nome} jogou? '))

      gols = []
      dados['gols'] = gols
      
      for i in range(0, quantas):
            goll= int(input(f'   Quantos gols na partida {i+1}: '))
            gols.append(goll)

      galera.append(dados.copy())
      dados.clear()         

      while True:
            resp = input('Quer continuar? [S/N]: ').upper()[0]
            if resp in 'SN':
                  break
            print('ERRO! Responda apenas S ou N.')
      if resp == 'N':
            break

print('-=-' * 30)
print(f'{'Codº':<} {'NOME':^10} {'Gols':>15} {'Total':>20}')
print('-=-' * 30)

print(galera)
for k, v in enumerate(galera):
      print(f'{k:}       ', end='')
      for d in v.values():
          print(f'{str(d):<20}', end='')
      print()

while True:
      n = int(input('Mostrar as notas de qual jogador? [999 PARAR]: '))
      if n == 999:
            break
      if n >= len(galera):
            print(f'Erro! Não existe jogador com o código {n}')
      else:
            print(f'-- LEVANTAMENTO DO JOGADOR {galera[n]['nome']}:')
            for indice, g in enumerate(galera[n]['gols']):
                  print(f'   => Na partida {indice + 1}, fez {g} gols')
            
print()
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
print()
