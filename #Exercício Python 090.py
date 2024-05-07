#Exercício Python 090

print()

dados = {}

nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))
print('-=-' * 30)

dados['Nome'] = nome
dados['média'] = media

if media < 5:
      dados['situação'] = 'Reprovado'
elif 5 > media < 7:
      dados['situação'] = 'Recuperação'
elif media > 7:
      dados['situação'] = 'Aprovado'

for key, value in dados.items():
      print(f' - {key} = {value} ')

print()

