#Exercício Python 041: 

#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

print()

from datetime import date

anoNascimento = int(input('Qual ano de nascimento do atleta? '))

idade = date.today().year - anoNascimento

print(f'O atleta tem {idade} anos.')
# print(f'Classificação: {}.')

if idade <= 9:
      print(f'Classificação: MIRIM.')

elif 9 < idade <= 14:
      print(f'Classificação: INFANTIL.')

elif 14 < idade <= 19:
      print(f'Classificação: JÚNIOR.')

elif 19 < idade <= 25:
      print(f'Classificação: SÊNIOR.')

elif idade > 25:
      print(f'Classificação: Master.')

print()