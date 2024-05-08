#Exercício Python 092

print()

from datetime import date
#print(date.today().year) ano de hoje

#36 anos de apoosentadoria

dados = {}

dados['Nome'] = nome = input('Nome: ')
nasci = int(input('Ano de nascimento: '))
idade = date.today().year - nasci
dados['idade'] = idade
dados['ctps'] = clt = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] == 0:
      print('ctps tem o valor 0')
else:
      dados['contratação'] = contrat = int(input('Ano de contratação: '))
      dados['salário'] = sal = float(input('salário: R$'))
      apo = date.today().year - dados['contratação']
      falta = 36 - apo
      dados['aposentadoria'] = falta + idade

print('-=-' * 20)

for key, value in dados.items():
      print(f' -{key} tem o valor {value}')
      
print()